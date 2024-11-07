<template>
    <div>
        <DataTable v-model:filters="filters" :value="users" paginator :loading="loading" :rows="5"
            :rowsPerPageOptions="[5, 10, 20, 50]" filterDisplay="menu"
            :globalFilterFields="['full_name', 'username', 'email', 'roles']" tableStyle="min-width: 50rem">
            <template #header>
                <div class="flex flex-wrap justify-between">
                    <Button type="button" icon="pi pi-filter-slash" label="Remover Filtro" outlined
                        @click="clearFilter()" />
                    <IconField>
                        <InputIcon>
                            <i class="pi pi-search" />
                        </InputIcon>
                        <InputText v-model="filters['global'].value" placeholder="Procurar" />
                    </IconField>
                </div>
            </template>
            <template #empty> Nenhum usuário encontrado. </template>
            <template #loading> Carregando Usuários. Por favor aguarde. </template>
            <Column field="full_name" header="Nome" maxConstraints="99" style="width: 30%">
                <template #body="{ data }">
                    <span>{{ formatNome(data.full_name) }}</span>
                </template>
                <template #filter="{ filterModel }">
                    <InputText v-model="filterModel.value" type="text" placeholder="Procurar por nome" />
                </template>
            </Column>
            <Column field="username" header="Usuário" maxConstraints="99" style="width: 15%">
                <template #body="{ data }">
                    <span>{{ data.username }}</span>
                </template>
                <template #filter="{ filterModel }">
                    <InputText v-model="filterModel.value" type="text" placeholder="Procurar por usuário" />
                </template>
            </Column>
            <Column field="email" header="E-Mail" maxConstraints="99" style="width: 15%">
                <template #body="{ data }">
                    <span>{{ data.email }}</span>
                </template>
                <template #filter="{ filterModel }">
                    <InputText v-model="filterModel.value" type="text" placeholder="Procurar por e-mail" />
                </template>
            </Column>
            <Column field="roles" header="Grupos" maxConstraints="99" :showFilterMatchModes="false" style="width: 15%">
                <template #body="slotProps">
                    <div class="flex flex-wrap gap-1">
                        <Tag v-for="role in slotProps.data.roles" :key="role" :severity="getTagSeverity(role)"
                            :value="getTagLabel(role)" />
                    </div>
                </template>
                <template #filter="{ filterModel }">
                    <Select v-model="filterModel.value" :options="roles" placeholder="Selecione um Grupo" showClear>
                        <template #value="slotProps">
                            <Tag v-if="slotProps.value" :key="slotProps.value"
                                :severity="getTagSeverity(slotProps.value)" :value="getTagLabel(slotProps.value)" />
                        </template>
                        <template #option="slotProps">
                            <Tag :key="slotProps.option" :severity="getTagSeverity(slotProps.option)"
                                :value="getTagLabel(slotProps.option)" />
                        </template>
                    </Select>
                </template>
            </Column>
            <Column style="width: 10%">
                <template #header="slotProps">
                    <div class="flex flex-wrap justify-end w-full">
                        <Button icon="pi pi-plus" label="Novo Usuário" @click="activateAddEditor" />
                    </div>
                </template>
                <template #body="slotProps">
                    <div class="flex justify-end">
                        <Button @click="activateEditEditor(slotProps.data)" icon="pi pi-pencil" text
                            aria-label="Edit" />
                        <Button @click="cloneUser(slotProps.data)" icon="pi pi-clone" severity="info" text
                            aria-label="Clone" />
                        <Button @click="deleteUser(slotProps.data)" icon="pi pi-trash" severity="danger" text
                            aria-label="Delete" />
                    </div>
                </template>
            </Column>
        </DataTable>

        <Dialog :closable="editor.closable" v-model:visible="editor.visible" modal :header="editor.header"
            :style="{ width: '50rem' }" :breakpoints="{ '1199px': '75vw', '575px': '90vw' }">
            <span class="text-surface-500 dark:text-surface-400 block mb-8">{{ editor.help }}</span>

            <label class="block mb-2 font-semibold w-24">Nome</label>
            <InputText placeholder="Nome" v-model="editor.first_name" @keypress="preventNumbers" maxlength="40"
                class="mb-4" fluid />

            <label class="block mb-2 font-semibold w-24">Sobrenome</label>
            <InputText placeholder="Sobrenome" v-model="editor.last_name" @keypress="preventNumbers" maxlength="40"
                class="mb-4" fluid />

            <label class="block mb-2 font-semibold w-24">E-Mail</label>
            <InputText placeholder="E-Mail" v-model="editor.email" maxlength="120"
                :class="{ 'border-red-500': emailError }" @blur="validateEmail" @input="validateEmail" fluid />
            <p v-if="emailError" class="text-red-500 text-sm">{{ emailError }}</p>

            <label class="block mb-2 font-semibold w-24 mt-4">Usuário</label>
            <InputText :placeholder="editor.username_placeholder" v-model="editor.username" maxlength="60" class="mb-4"
                fluid />

            <label class="block mb-2 font-semibold w-24">Senha</label>
            <Password v-model="editor.password" :placeholder="editor.password_placeholder" :toggleMask="true"
                class="mb-4" fluid :feedback="false" @input="validatePassword" />

            <label class="block mb-2 font-semibold w-24">Grupos</label>
            <PickList class="mb-8" v-model="editor.roles" breakpoint="1400px">
                <template #option="slotProps">
                    <Tag :key="slotProps.option" :severity="getTagSeverity(slotProps.option)"
                        :value="getTagLabel(slotProps.option)" />
                </template>
            </PickList>

            <div class="flex justify-end gap-2">
                <Button type="button" :loading="editor.loading" label="Cancelar" severity="secondary"
                    @click="editor.visible = false"></Button>
                <Button v-if="editor.mode == 'add'" :loading="editor.loading" type="button" label="Salvar"
                    @click="addUser"></Button>
                <Button v-if="editor.mode == 'edit'" :loading="editor.loading" type="button" label="Editar"
                    @click="editUser"></Button>
            </div>
        </Dialog>
    </div>
</template>

<script>
import { FilterMatchMode, FilterOperator } from '@primevue/core/api';
import { useRouter } from 'vue-router';
import { api } from '@/service/api';
import { handleUserErrors } from '@/common/utils';

export default {
    data() {
        return {
            router: useRouter(),
            users: null,
            roles: [
                'user',
                'rh',
                'admin'
            ],
            filters: null,
            loading: false,
            editor: {},
        };
    },
    methods: {
        preventNumbers(event) {
            const regex = /^[a-zA-ZÀ-ÿ\s]*$/; 
            if (!regex.test(event.key)) {
                event.preventDefault();
            };
        },
        validateEmail() {
            const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/; 
            if (!emailRegex.test(this.editor.email)) {
                this.emailError = 'E-mail inválido';
            } else {
                this.emailError = '';
            }
        },
        validatePassword(event) {
            const maxLength = 30;
            if (event.target.value.length > maxLength) {
                event.target.value = event.target.value.slice(0, maxLength);
                this.editor.password = event.target.value;
            }
        },
        formatNome(input) {
            if (!input) return input;

            let formattedInput = input
                .toLowerCase()
                .split(' ')
                .map(word => word.charAt(0).toUpperCase() + word.slice(1))
                .join(' ');

            if (formattedInput.length > 30) {
                formattedInput = formattedInput.substring(0, 26) + "...";
            }

            return formattedInput;
        },
        getTagSeverity(role) {
            switch (role) {
                case 'admin':
                    return 'danger';
                case 'rh':
                    return 'info';
                case 'user':
                    return 'success';
                default:
                    return 'secondary';
            }
        },
        getTagLabel(role) {
            switch (role) {
                case 'admin':
                    return 'Administrador';
                case 'rh':
                    return 'RH';
                case 'user':
                    return 'Usuário';
                default:
                    return role;
            }
        },
        clearUsers() {
            this.loading = true;

            api.getUsers()
                .then(response => {
                    this.users = response.data;
                    this.clearFilter();
                    this.loading = false;
                })
                .catch(error => {
                    handleUserErrors(error, this.$router, this.$toast)
                });

        },
        clearFilter() {
            this.filters = {
                global: { value: null, matchMode: FilterMatchMode.CONTAINS },
                full_name: { operator: FilterOperator.AND, constraints: [{ value: null, matchMode: FilterMatchMode.STARTS_WITH }] },
                username: { operator: FilterOperator.AND, constraints: [{ value: null, matchMode: FilterMatchMode.STARTS_WITH }] },
                email: { operator: FilterOperator.AND, constraints: [{ value: null, matchMode: FilterMatchMode.STARTS_WITH }] },
                roles: { operator: FilterOperator.OR, constraints: [{ value: null, matchMode: FilterMatchMode.CONTAINS }] },
            };
        },
        activateAddEditor() {
            this.editor = {
                visible: true,
                closable: true,
                loading: false,
                mode: 'add',
                header: 'Novo Usuário',
                help: 'Informe os dados necessários',
                username_placeholder: 'Usuário',
                username: '',
                password_placeholder: 'Senha',
                password: '',
                first_name: '',
                last_name: '',
                email: '',
                emailError: '',
                roles: [
                    [
                        'rh',
                        'admin'
                    ],
                    []
                ]
            }
        },
        activateEditEditor(user) {
            this.editor = {
                visible: true,
                closable: true,
                loading: false,
                mode: 'edit',
                header: 'Editar Usuário',
                help: 'Informe os dados atualizados',
                original_username: user.username,
                username_placeholder: 'Deixe em branco para manter o usuário atual',
                username: '',
                password_placeholder: 'Deixe em branco para manter a senha atual',
                password: '',
                first_name: user.first_name,
                last_name: user.last_name,
                email: user.email,
                roles: [
                    this.roles.filter(role => !user.roles.includes(role)),
                    user.roles.filter(role => role !== 'user')
                ]
            }
        },
        addUser() {
            this.editor.closable = false;
            this.editor.loading = true;

            let data = {
                username: this.editor.username,
                password: this.editor.password,
                first_name: this.editor.first_name,
                last_name: this.editor.last_name,
                email: this.editor.email,
                roles: ['user', ...this.editor.roles[1]]
            }

            api.postAddUser(data)
                .then(response => {
                    this.editor.closable = true;
                    this.editor.visible = false;
                    this.clearUsers();
                })
                .catch(error => {
                    handleUserErrors(error, this.$router, this.$toast)
                    this.editor.closable = true;
                    this.editor.loading = false;
                });
        },
        editUser() {
            this.editor.closable = false;
            this.editor.loading = true;

            let data = {
                first_name: this.editor.first_name,
                last_name: this.editor.last_name,
                email: this.editor.email,
                roles: ['user', ...this.editor.roles[1]]
            }

            if (this.editor.username != '') {
                data.username = this.editor.username;
            }

            if (this.editor.password != '') {
                data.password = this.editor.password;
            }

            api.postEditUser(data, this.editor.original_username)
                .then(response => {
                    this.editor.closable = true;
                    this.editor.visible = false;
                    this.clearUsers();
                })
                .catch(error => {
                    handleUserErrors(error, this.$router, this.$toast)
                    this.editor.closable = true;
                    this.editor.loading = false;
                });
        },
        deleteUser(user) {
            this.$confirm.require({
                message: `Você tem certeza de que deseja excluir o usuário ${this.formatNome(user.full_name)}?`,
                header: 'Ação Irreversível',
                icon: 'pi pi-exclamation-triangle',
                rejectProps: {
                    label: 'Cancelar',
                    severity: 'secondary',
                    outlined: true
                },
                acceptProps: {
                    label: 'Excluir',
                    severity: 'danger'
                },
                accept: () => {
                    this.loading = true;

                    api.deleteUser(user.username)
                        .then(response => {
                            this.clearUsers();
                            this.$toast.add({ severity: 'info', summary: 'Exclusão Confirmada', detail: `Usuário ${this.formatNome(user.full_name)} excluído com sucesso`, life: 10000 });
                        })
                        .catch(error => {
                            handleUserErrors(error, this.$router, this.$toast)
                            this.loading = false;
                        });
                },
                reject: () => {
                    this.$toast.add({ severity: 'warn', summary: 'Ação Cancelada', detail: `Você desistiu da exclusão do usuário ${this.formatNome(user.full_name)}`, life: 10000 });
                }
            });
        },
        cloneUser(user) {
            this.loading = true;

            let data = {
                username: user.username
            }

            api.postCloneUser(data)
                .then(response => {
                    this.clearUsers();
                })
                .catch(error => {
                    handleUserErrors(error, this.$router, this.$toast)
                    this.loading = false;
                });
        }
    },
    created() {
        this.clearFilter();
    },
    mounted() {
        this.clearUsers();
    }
}
</script>
