<template>
    <DataTable v-model:filters="filters" :value="stores" paginator :loading="loading" :rows="5"
        :rowsPerPageOptions="[5, 10, 20, 50]" filterDisplay="menu" :globalFilterFields="['name']"
        tableStyle="min-width: 50rem">
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
        <template #empty> Nenhuma loja encontrada. </template>
        <template #loading> Carregando Lojas. Por favor aguarde. </template>
        <Column field="name" header="Nome" maxConstraints="99" style="width: 80%">
            <template #body="{ data }">
                <Tag :value="formatNome(data.name)" :severity="data.color" />
            </template>
        </Column>
        <Column style="width: 10%; ">
            <template #header="slotProps">
                <div class="flex flex-wrap justify-end w-full">
                    <Button icon="pi pi-plus" label="Nova Loja" @click="activateAddEditor" />
                </div>
            </template>
            <template #body="slotProps">
                <div class="flex justify-end">
                    <Button @click="activateEditEditor(slotProps.data)" icon="pi pi-pencil" text aria-label="Edit" />
                    <Button @click="deleteStore(slotProps.data)" icon="pi pi-trash" severity="danger" text
                        aria-label="Delete" />
                </div>
            </template>
        </Column>
    </DataTable>


    <Dialog :closable="editor.closable" v-model:visible="editor.visible" modal :header="editor.header"
        :style="{ width: '50rem' }" :breakpoints="{ '1199px': '75vw', '575px': '90vw' }">
        <span class="text-surface-500 dark:text-surface-400 block mb-8">{{ editor.help }}</span>

        <div class="flex gap-3 w-full mb-6">
            <div class="w-full">
                <label class="block font-semibold w-24 mt-2 mb-2">Nome</label>
                <InputText placeholder="Nome" v-model="editor.name" maxlength="80" class="mb-4" fluid />
            </div>
            <div class="w-min">
                <label class="block font-semibold w-24 mt-2 mb-2">Cor</label>
                <Select v-model="editor.color" :options="colors" optionLabel="name" optionValue="value"
                    placeholder="Selecione uma cor" class=" md:w-56 mb-4" fluid>
                    <template #value="slotProps">
                        <Tag v-if="slotProps.value" :key="slotProps.value" :severity="slotProps.value"
                            :value="getColorByValue(slotProps.value)" />
                    </template>
                    <template #option="slotProps">
                        <Tag :key="slotProps.option" :severity="slotProps.option.value"
                            :value="slotProps.option.name" />
                    </template>
                </Select>
            </div>
        </div>



        <div class="flex justify-end gap-2">
            <Button type="button" :loading="editor.loading" label="Cancelar" severity="secondary"
                @click="editor.visible = false"></Button>
            <Button v-if="editor.mode == 'add'" :loading="editor.loading" type="button" label="Salvar"
                @click="addStore"></Button>
            <Button v-if="editor.mode == 'edit'" :loading="editor.loading" type="button" label="Editar"
                @click="editStore"></Button>
        </div>
    </Dialog>


</template>

<script>
import { FilterMatchMode, FilterOperator } from '@primevue/core/api';
import { useRouter } from 'vue-router';
import { api } from '@/service/api';
import { handleStoreErrors } from '@/common/utils';

export default {
    data() {
        return {
            router: useRouter(),
            stores: null,
            filters: null,
            loading: false,
            editor: {},
            colors: [
                { name: 'Primária', value: "primary" },
                { name: 'Secundária', value: "secondary" },
                { name: 'Sucesso', value: "success" },
                { name: 'Informação', value: "info" },
                { name: 'Aviso', value: "warn" },
                { name: 'Perigo', value: "danger" },
                { name: 'Contraste', value: "contrast" },
            ],
        };
    },
    methods: {
        clearStores() {
            this.loading = true;

            api.getStores()
                .then(response => {
                    this.stores = response.data;
                    this.clearFilter();
                    this.loading = false;
                })
                .catch(error => {
                    handleStoreErrors(error, this.$router, this.$toast)
                });
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
        getColorByValue(input) {
            if (!input) return input;

            if (input === "primary") return "Primária";
            if (input === "secondary") return "Secundária";
            if (input === "success") return "Sucesso";
            if (input === "info") return "Informação";
            if (input === "warn") return "Aviso";
            if (input === "danger") return "Perigo";
            if (input === "contrast") return "Contraste";

            return input;
        },
        clearFilter() {
            this.filters = {
                global: { value: null, matchMode: FilterMatchMode.CONTAINS },
            };
        },
        activateAddEditor() {
            this.editor = {
                visible: true,
                closable: true,
                loading: false,
                mode: 'add',
                header: 'Nova Loja',
                help: 'Informe o nome da loja que deseja cadastrar e sua respectiva cor'
            }
        },
        activateEditEditor(store) {
            this.editor = {
                visible: true,
                closable: true,
                loading: false,
                mode: 'edit',
                header: 'Editar Loja',
                help: 'Informe os dados atualizados',
                id: store.id,
                name: store.name,
                color: store.color,
            }
        },
        addStore() {
            this.editor.closable = false;
            this.editor.loading = true;

            let data = { name: this.editor.name, color: this.editor.color }

            api.postAddStore(data)
                .then(response => {
                    this.editor.closable = true;
                    this.editor.visible = false;
                    this.clearStores();
                })
                .catch(error => {
                    handleStoreErrors(error, this.$router, this.$toast)
                    this.editor.closable = true;
                    this.editor.loading = false;
                });
        },
        editStore() {
            this.editor.closable = false;
            this.editor.loading = true;

            let data = { name: this.editor.name, color: this.editor.color }

            if (this.editor.name != '') {
                data.name = this.editor.name;
            }

            api.postEditStore(data, this.editor.id)
                .then(response => {
                    this.editor.closable = true;
                    this.editor.visible = false;
                    this.clearStores();
                })
                .catch(error => {
                    handleStoreErrors(error, this.$router, this.$toast)
                    this.editor.closable = true;
                    this.editor.loading = false;
                });
        },
        deleteStore(store) {
            this.$confirm.require({
                message: `Você tem certeza de que deseja excluir a ${this.formatNome(store.name)}?`,
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

                    api.deleteStore(store.id)
                        .then(response => {
                            this.clearStores();
                        })
                        .catch(error => {
                            handleStoreErrors(error, this.$router, this.$toast)
                            this.loading = false;
                        });

                    this.$toast.add({ severity: 'info', summary: 'Exclusão Confirmada', detail: `${this.formatNome(store.name)} excluída com sucesso`, life: 10000 });
                },
                reject: () => {
                    this.$toast.add({ severity: 'warn', summary: 'Ação Cancelada', detail: `Você desistiu da exclusão da ${this.formatNome(store.name)}`, life: 10000 });
                }
            });
        },
    },
    created() {
        this.clearFilter();
    },
    mounted() {
        this.clearStores();
    }
}
</script>
