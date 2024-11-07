<template>
    <Message class="mb-3" severity="warn" closable>
        Contratações só podem ser feitas via banco de dados oficial da nossa Empresa. Entrevistas devem ser conduzidas por
        profissionais capacitados do RH e todos os tópicos devem ser devimente preenchidos.
    </Message>

    <div class="card">
        <div>
            <IconField>
                <InputIcon :class="icon" />
                <InputMask v-model="value" fluid @update:modelValue="searchCurriculo" autoClear :disabled="loading"
                    mask="999.999.999-99" placeholder="Buscar Currículo por CPF..." />
            </IconField>
        </div>

        <div v-if="loading" class="flex items-center justify-center" style="min-height: 36rem;">
            <ProgressSpinner style="width: 50px; height: 50px" />
        </div>
        <div v-else class="flex items-center justify-center" style="min-height: 36rem;">
            <div>
                <img src="/src/busca.svg" alt="Logo" style="height: auto;" />
            </div>
        </div>
    </div>

    <Dialog v-if="curriculo" @hide="hideDialog" v-model:visible="visible" modal :style="{ width: '50rem' }"
        :breakpoints="{ '1199px': '75vw', '575px': '90vw' }">
        <template #header>
            <div class="inline-flex items-center gap-2 w-full">
                <div v-if="!curriculo.foto">
                    <Avatar icon="pi pi-user" size="large" shape="circle" />
                </div>
                <div v-else>
                    <Image alt="Image" preview>
                        <template #image>
                            <Avatar :image="'http://127.0.0.1:8000/' + curriculo.foto.foto" size="large" shape="circle" />
                        </template>
                        <template #preview="slotProps">
                            <img :src="'http://127.0.0.1:8000/' + curriculo.foto.foto" alt="preview" :style="slotProps.style"
                                @click="slotProps.onClick" />
                        </template>
                    </Image>
                </div>
                <div class="flex justify-center w-full">
                    <Tag :value="'Ultima atualização: ' + formatDateTime(curriculo.ultima_atualizacao)"
                        :severity="getSeverityDate(curriculo.ultima_atualizacao)" />
                </div>
            </div>
        </template>
        <div class="flex flex-col gap-2 mx-auto" style="max-width: 40rem">
            <div class="text-center mt-4 mb-8 text-xl font-semibold">Dados Pessoais</div>
            <div class="flex flex-row flex-wrap gap-3">
                <div class="flex-1">
                    <div class="flex flex-col mb-6">
                        <FloatLabel>
                            <InputText readonly maxlength="200" fluid v-model="curriculo.nome" />
                            <label>Nome</label>
                        </FloatLabel>
                    </div>
                </div>
                <div class="flex-1">
                    <div class="flex flex-col mb-6">
                        <FloatLabel>
                            <InputNumber readonly v-model="curriculo.idade" fluid />
                            <label>Idade</label>
                        </FloatLabel>
                    </div>
                </div>
            </div>
            <div class="flex flex-row flex-wrap gap-3">
                <div class="flex-1">
                    <div class="flex flex-col mb-6">
                        <FloatLabel>
                            <InputMask readonly mask="999.999.999-99" v-model="curriculo.cpf" fluid />
                            <label>CPF</label>
                        </FloatLabel>
                    </div>
                </div>
                <div class="flex-1">
                    <FloatLabel>
                        <InputMask readonly v-model="curriculo.rg" mask="9999?9999-99" placeholder="99999999-99" fluid />
                        <label>RG</label>
                    </FloatLabel>
                </div>
            </div>
            <div class="flex flex-row flex-wrap gap-3">
                <div class="flex-1">
                    <div class="flex flex-col mb-6">
                        <FloatLabel>
                            <InputMask readonly v-model="curriculo.telefone" mask="(99) 9999-9999?9" placeholder="(99) 9999-99999" fluid />
                            <label>Telefone 1</label>
                        </FloatLabel>
                    </div>
                </div>
                <div class="flex-1">
                    <div class="flex flex-col mb-6">
                        <FloatLabel>
                            <InputMask readonly v-model="curriculo.telefone_adicional" mask="(99) 9999-9999?9"
                                placeholder="(99) 9999-99999" fluid />
                            <label>Telefone 2</label>
                        </FloatLabel>
                    </div>
                </div>
            </div>
            <div class="flex flex-row flex-wrap gap-3">
                <div class="flex-1 mb-6">
                    <FloatLabel>
                        <DatePicker style="min-width: 200px;" v-model="curriculo.data_de_nascimento" showIcon fluid
                            :showOnFocus="false" />
                        <label>Data de nascimento</label>
                    </FloatLabel>
                </div>
                <div class="flex-1 mb-6">
                    <FloatLabel>
                        <Select disabled v-model="curriculo.estado_civil" :options="estado_civil" fluid />
                        <label>Estado Civil</label>
                    </FloatLabel>
                </div>
            </div>
            <div class="flex flex-row flex-wrap gap-3">
                <div class="flex-1 mb-2">
                    <FloatLabel>
                        <Select disabled v-model="curriculo.escolaridade" :options="escolaridade" fluid />
                        <label>Escolaridade</label>
                    </FloatLabel>
                </div>
                <div class="flex-1 mb-6">
                    <ToggleButton readonly class="w-full" v-model="curriculo.possui_cursos_complementares"
                        onLabel="Possui Cursos Complementares" offLabel="Não Possui Cursos Complementares"
                        @change="changeCursosComplementares" />
                </div>
            </div>
            <FloatLabel class="mb-2">
                <Textarea readonly maxlength="450" v-model="curriculo.cursos_observacao" fluid rows="3" cols="30" />
                <label>Cursos Complementares</label>
            </FloatLabel>
        </div>
        <div class="flex flex-col gap-2 mx-auto" style="max-width: 40rem">
            <div class="text-center mt-4 mb-4 text-xl font-semibold">Currículo e Apresentação Pessoal</div>
            <div class="flex justify-center gap-2 mb-4">
                <Image v-if="curriculo.curriculo" :src="'http://127.0.0.1:8000/' + curriculo.curriculo.foto" alt="Image" preview />
            </div>
            <div class="flex justify-between gap-2 mb-2">
                <label>Estado do Currículo</label>
                <div class="flex flex-col gap-2">
                    <div class="flex justify-end">
                        <Rating readonly v-model="curriculo.apresentacao_curriculo" />
                    </div>
                </div>
            </div>
            <div class="flex justify-between gap-2 mb-2">
                <label>Apresentação Pessoal</label>
                <div class="flex flex-col gap-2">
                    <div class="flex justify-end">
                        <Rating readonly v-model="curriculo.apresentacao_pessoal" />
                    </div>
                </div>
            </div>
            <div class="flex flex-col gap-2 mt-8">
                <FloatLabel>
                    <Textarea readonly maxlength="450" v-model="curriculo.apresentacao_observacao" fluid rows="5"
                        cols="30" />
                    <label>Observações (Apresentação)</label>
                </FloatLabel>
            </div>
        </div>
        <div class="flex flex-col gap-2 mx-auto" style="max-width: 40rem">
            <div class="text-center mt-9 mb-8 text-xl font-semibold">Dependentes</div>

            <div class="flex flex-row flex-wrap gap-3">
                <div class="flex-1 mb-6">
                    <ToggleButton readonly class="w-full" v-model="curriculo.possui_dependentes"
                        onLabel="Possui Dependentes" offLabel="Não Possui Dependentes"
                        @change="changePossuiDependentes" />
                </div>
                <div class="flex-1 mb-6">
                    <FloatLabel>
                        <InputNumber readonly v-model="curriculo.numero_dependentes" fluid />
                        <label>N° Dependentes</label>
                    </FloatLabel>
                </div>
            </div>
            <div class="flex flex-col mb-6">
                <FloatLabel>
                    <Textarea readonly v-model="curriculo.observacao_dependentes" fluid rows="5" cols="30" />
                    <label>Observações (Idade, Necessidades Especiais)</label>
                </FloatLabel>
            </div>
        </div>
        <div class="flex flex-col gap-2 mx-auto" style="max-width: 40rem">
            <div class="text-center mt-4 mb-8 text-xl font-semibold">Endereço</div>
            <div class="flex flex-row flex-wrap gap-3">
                <div class="flex-1">
                    <div class="flex flex-col mb-6">
                        <FloatLabel>
                            <InputMask readonly v-model="curriculo.cep" mask="99999-999" placeholder="99999-999"
                                fluid />
                            <label class="w-full pr-7">
                                <div class="flex justify-between">
                                    <div>
                                        CEP
                                    </div>
                                    <div>
                                        <i v-if="loadingCep" class="pi pi-spin pi-spinner mt-8"></i>
                                    </div>
                                </div>
                            </label>
                        </FloatLabel>
                    </div>
                </div>
                <div class="flex-1">
                    <div class="flex flex-col mb-6">
                        <FloatLabel>
                            <Select disabled v-model="curriculo.uf" :options="ufs" fluid />
                            <label>Unidade Federativa</label>
                        </FloatLabel>
                    </div>
                </div>
            </div>
            <div class="flex flex-row flex-wrap gap-3">
                <div class="flex-1">
                    <div class="flex flex-col mb-6">
                        <FloatLabel>
                            <InputText readonly maxlength="150" fluid v-model="curriculo.cidade" />
                            <label>Cidade</label>
                        </FloatLabel>
                    </div>
                </div>
                <div class="flex-1">
                    <div class="flex flex-col mb-6">
                        <FloatLabel>
                            <InputText readonly maxlength="150" fluid v-model="curriculo.bairro" />
                            <label>Bairro</label>
                        </FloatLabel>
                    </div>
                </div>
            </div>
            <div class="flex flex-row flex-wrap gap-3">
                <div class="flex-1">
                    <div class="flex flex-col mb-6">
                        <FloatLabel>
                            <InputText readonly maxlength="250" fluid v-model="curriculo.rua" />
                            <label>Rua</label>
                        </FloatLabel>
                    </div>
                </div>
                <div class="flex-1">
                    <FloatLabel>
                        <InputNumber readonly v-model="curriculo.numero" inputId="minmax" :min="1" :max="999999"
                            fluid />
                        <label>Número</label>
                    </FloatLabel>
                </div>
            </div>
            <FloatLabel class="mb-6">
                <InputText readonly maxlength="250" fluid v-model="curriculo.complemento" />
                <label>Complemento</label>
            </FloatLabel>
        </div>
        <div class="flex flex-col gap-2 mx-auto" style="max-width: 40rem">
            <div class="text-center mt-4 mb-8 text-xl font-semibold">Experiência</div>
            <ToggleButton readonly class="w-full mb-6" v-model="curriculo.possui_experiencia"
                onLabel="Possui Experiência Profissional" offLabel="Não Possui Experiência Profissional"
                @change="changePossuiExperiencia" />
            <div class="flex justify-between gap-2">
                <label>Experiência Profissional Anterior.</label>
                <div class="flex flex-col gap-2">
                    <div class="flex justify-end">
                        <Rating readonly v-model="curriculo.relato_experiencia" />
                    </div>
                    <div class="flex justify-end">
                    </div>
                </div>
            </div>
            <div class="flex justify-between gap-2 mt-5 mb-8">
                <label>Motivo da Saída dos Empregos Anteriores.</label>
                <div class="flex flex-col gap-2">
                    <div class="flex justify-end">
                        <Rating readonly v-model="curriculo.relato_desligamento" />
                    </div>
                </div>
            </div>
            <div class="flex flex-col mb-6">
                <FloatLabel>
                    <Textarea readonly maxlength="450" v-model="curriculo.observacao_experiencia" fluid rows="5"
                        cols="30" />
                    <label>Observações (Empresas anteriores, Cargos, etc.)</label>
                </FloatLabel>
            </div>
        </div>
        <div class="flex flex-col gap-2 mx-auto" style="max-width: 40rem">
            <div class="text-center mt-4 mb-8 text-xl font-semibold">Entrevista</div>
            <div class="flex justify-between gap-2 mb-1">
                <label>Por que você gostaria de trabalhar na nossa Empresa?</label>
                <div class="flex flex-col gap-2">
                    <div class="flex justify-end">
                        <Rating readonly v-model="curriculo.relato_motivacao" />
                    </div>
                </div>
            </div>
            <label class="mb-6">Quais Lojas/Setores você tem interesse em atuar? Escolha até
                2 opções.</label>
            <div class="flex flex-row flex-wrap gap-3 mb-2">
                <div class="flex-1">
                    <div class="flex flex-col">
                        <FloatLabel>
                            <MultiSelect disabled v-model="curriculo.view_lojas_interesse" :options="lojas"
                                optionLabel="name" class="w-full" />
                            <label for="ms-cities">Lojas</label>
                        </FloatLabel>
                    </div>
                </div>
                <div class="flex-1">
                    <div class="flex flex-col">
                        <FloatLabel>
                            <MultiSelect disabled v-model="curriculo.view_setores_interesse" :options="setores"
                                optionLabel="name" class="w-full" />
                            <label for="ms-cities">Setores</label>
                        </FloatLabel>
                    </div>
                </div>
            </div>
            <div class="flex justify-between gap-2 mb-6">
                <label>Por que você escolheu essas lojas/setores?</label>
                <div class="flex flex-col gap-2">
                    <div class="flex justify-end">
                        <Rating readonly v-model="curriculo.relato_interesse" />
                    </div>
                    <div class="flex justify-end">
                    </div>
                </div>
            </div>
            <div class="flex justify-between gap-2 mb-2">
                <label>Você prefere trabalhar em grupo ou sozinho? Por quê?</label>
                <div class="flex flex-col gap-2">
                    <div class="flex justify-end">
                        <Rating readonly v-model="curriculo.relato_equipe" />
                    </div>
                </div>
            </div>
            <ToggleButton readonly class="w-full mb-6" v-model="curriculo.restricoes_horario"
                onLabel="Possui Restrição de Horário" offLabel="Não Possui Restrição de Horário" />
            <div class="flex flex-col mb-4">
                <FloatLabel>
                    <Textarea readonly maxlength="450" v-model="curriculo.observacoes_entrevista" fluid rows="3"
                        cols="30" />
                    <label>Observações (Restrições de horário, etc.)</label>
                </FloatLabel>
            </div>
        </div>
        <div class="flex flex-col gap-2 mx-auto" style="max-width: 40rem">
            <div class="text-center mt-6 mb-8 text-xl font-semibold">Considerações Finais</div>
            <div class="flex flex-col mb-1">
                <FloatLabel>
                    <InputText readonly fluid v-model="curriculo.entrevistador" />
                    <label>Nome do Entrevistador</label>
                </FloatLabel>
            </div>
            <label class="mb-6">Quais Setores combinam com o perfil do candidato?</label>
            <div class="flex-1">
                <div class="flex flex-col mb-2">
                    <FloatLabel>
                        <MultiSelect disabled v-model="curriculo.view_setores_ideal" :options="setores"
                            optionLabel="name" class="w-full" />
                        <label for="ms-cities">Setores</label>
                    </FloatLabel>
                </div>
            </div>
            <ToggleButton readonly class="w-full mb-2" v-model="curriculo.apto_contratacao"
                onLabel="Está Apto Para Contratação" offLabel="Não Está Apto Para Contratação" />
            <ToggleButton readonly class="w-full mb-2" v-model="curriculo.ex_funcionario" onLabel="É Ex-Funcionário"
                offLabel="Não É Ex-Funcionário" />
            <ToggleButton readonly class="w-full mb-6" v-model="curriculo.atualmente_contratado"
                onLabel="É Colaborador Atualmente" offLabel="Não é Colaborador Atualmente" />

            <FloatLabel class="mb-4">
                <Textarea readonly maxlength="450" v-model="curriculo.observacao" fluid rows="5" cols="30" />
                <label>Observações Finais</label>
            </FloatLabel>
        </div>
        <div class="flex flex-col gap-2 mx-auto" style="max-width: 40rem">
            <Button type="button" iconPos="right" icon="pi pi-save" label="Atualizar"
                @click="editCurriculo(curriculo)"></Button>
        </div>
    </Dialog>

</template>

<script>
import { handleSearchCurriculoErrors } from '@/common/utils';
import { api } from '@/service/api';

export default {
    data() {
        return {
            value: null,
            visible: false,
            value_aux: null,
            curriculo: null,
            icon: "pi pi-search",
            loading: false,
            estado_civil: [
                'Solteiro(a)',
                'Casado(a)',
                'Divorciado(a)',
                'Viúvo(a)',
                'Separado(a)',
                'União Estável',
                'Companheiro(a)',
                'Desquitado(a)',
                'Outro'
            ],
            escolaridade: [
                'Analfabeto(a)',
                'Alfabetizado(a)',
                'Ensino Fundamental Incompleto',
                'Ensino Fundamental Completo',
                'Ensino Médio Incompleto',
                'Ensino Médio Completo',
                'Técnico Incompleto',
                'Técnico Completo',
                'Superior Incompleto',
                'Superior Completo',
                'Pós-graduação Incompleta',
                'Pós-graduação Completa',
                'Mestrado Incompleto',
                'Mestrado Completo',
                'Doutorado Incompleto',
                'Doutorado Completo',
                'Pós-Doutorado',
                'Outro',
            ],
            ufs: [
                "Acre",  
                "Alagoas",  
                "Amapá",  
                "Amazonas", 
                "Bahia", 
                "Ceará",  
                "Distrito Federal", 
                "Espírito Santo",  
                "Goiás",  
                "Maranhão",  
                "Mato Grosso", 
                "Mato Grosso do Sul",  
                "Minas Gerais",  
                "Pará",  
                "Paraíba", 
                "Paraná",  
                "Pernambuco",  
                "Piauí",  
                "Rio de Janeiro",  
                "Rio Grande do Norte",  
                "Rio Grande do Sul",  
                "Rondônia",  
                "Roraima",  
                "Santa Catarina",  
                "São Paulo", 
                "Sergipe", 
                "Tocantins"  
            ],
            setores: [],

            lojas: [],
        }
    },
    methods: {
        cadastro() {
            this.$router.push(`/cadastrar-curriculo/${this.value}`);
        },
        getSeverityDate(input) {
            if (!input) return input;

            if (!(input instanceof Date) || isNaN(input)) {
                return "danger";
            }

            const currentDate = new Date();
            const timeDifference = currentDate - input; 
            const dayDifference = Math.floor(timeDifference / (1000 * 60 * 60 * 24)); 

            if (dayDifference < 90) {
                return "success";
            } else if (dayDifference <= 180) {
                return "primary";
            } else if (dayDifference <= 365) {
                return "warn";
            } else if (dayDifference <= 730) {
                return "danger"
            } else {
                return "contrast";
            }
        },
        formatDateTime(input) {
            if (!input) return input;

            if (!(input instanceof Date) || isNaN(input)) {
                return input; 
            }

            const day = String(input.getDate()).padStart(2, '0');
            const month = String(input.getMonth() + 1).padStart(2, '0'); 
            const year = input.getFullYear();

            const hours = String(input.getHours()).padStart(2, '0');
            const minutes = String(input.getMinutes()).padStart(2, '0');
            const seconds = String(input.getSeconds()).padStart(2, '0');

            const formattedDate = `${day}/${month}/${year} ${hours}:${minutes}:${seconds}`;
            return formattedDate;
        },
        searchCurriculo() {
            if (this.value) {
                if (typeof this.value === 'string') {
                    const numericValue = this.value.replace(/\D/g, '');

                    if (numericValue.length == 11 && this.value != this.value_aux) {
                        this.loading = true;
                        this.icon = "pi pi-spin pi-spinner";
                        this.value_aux = this.value;
                        api.getCurriculo(numericValue)
                            .then(response => {
                                this.curriculo = {};
                                this.curriculo.apresentacao_curriculo = response.data.apresentacao_curriculo;
                                this.curriculo.apresentacao_pessoal = response.data.apresentacao_pessoal;
                                this.curriculo.apresentacao_observacao = response.data.apresentacao_observacao;
                                if(response.data.foto) this.curriculo.foto = response.data.foto;
                                if(response.data.curriculo) this.curriculo.curriculo = response.data.curriculo;
                                this.curriculo.nome = response.data.nome;
                                this.curriculo.idade = response.data.idade;
                                this.curriculo.cpf = response.data.cpf;
                                this.curriculo.rg = response.data.rg;
                                this.curriculo.telefone = response.data.telefone;
                                this.curriculo.telefone_adicional = response.data.telefone_adicional;
                                this.curriculo.data_de_nascimento = new Date(response.data.data_de_nascimento);
                                this.curriculo.estado_civil = response.data.estado_civil;
                                this.curriculo.escolaridade = response.data.escolaridade;
                                this.curriculo.possui_cursos_complementares = response.data.possui_cursos_complementares;
                                this.curriculo.cursos_observacao = response.data.cursos_observacao;
                                this.curriculo.possui_dependentes = response.data.possui_dependentes;
                                this.curriculo.numero_dependentes = response.data.numero_dependentes;
                                this.curriculo.observacao_dependentes = response.data.observacao_dependentes;
                                this.curriculo.cep = response.data.cep;
                                this.curriculo.uf = response.data.uf;
                                this.curriculo.cidade = response.data.cidade;
                                this.curriculo.bairro = response.data.bairro;
                                this.curriculo.rua = response.data.rua;
                                this.curriculo.numero = response.data.numero;
                                this.curriculo.complemento = response.data.complemento;
                                this.curriculo.possui_experiencia = response.data.possui_experiencia;
                                this.curriculo.relato_experiencia = response.data.relato_experiencia;
                                this.curriculo.relato_desligamento = response.data.relato_desligamento;
                                this.curriculo.observacao_experiencia = response.data.observacao_experiencia;
                                this.curriculo.relato_motivacao = response.data.relato_motivacao;
                                this.curriculo.lojas_interesse = response.data.lojas_interesse;
                                this.curriculo.setores_interesse = response.data.setores_interesse;
                                this.curriculo.relato_interesse = response.data.relato_interesse;
                                this.curriculo.relato_equipe = response.data.relato_equipe;
                                this.curriculo.restricoes_horario = response.data.restricoes_horario;
                                this.curriculo.observacoes_entrevista = response.data.observacoes_entrevista;
                                this.curriculo.entrevistador = response.data.entrevistador;
                                this.curriculo.setores_ideal = response.data.setores_ideal;
                                this.curriculo.apto_contratacao = response.data.apto_contratacao;
                                this.curriculo.ex_funcionario = response.data.ex_funcionario;
                                this.curriculo.atualmente_contratado = response.data.atualmente_contratado;
                                this.curriculo.observacao = response.data.observacao;
                                this.curriculo.bate_perfil_setor = this.curriculo.setores_interesse.some(setorInteresse =>
                                    this.curriculo.setores_ideal.some(setorIdeal =>
                                        setorInteresse.id === setorIdeal.id
                                    ));
                                this.curriculo.ultima_atualizacao = new Date(response.data.ultima_atualizacao)
                                this.visible = true;
                                this.loading = false;
                                this.icon = "pi pi-search";
                            })
                            .catch(error => {
                                handleSearchCurriculoErrors(error, this.$router, this.$toast);
                                this.loading = false;
                                this.icon = "pi pi-search";
                                this.$confirm.require({
                                    message: `O CPF ${this.value} não foi encontrado no banco de currículos. Deseja cadastrar um novo currículo?`,
                                    header: 'Confirmação',
                                    icon: 'pi pi-exclamation-triangle',
                                    rejectProps: {
                                        label: 'Não',
                                        severity: 'secondary',
                                        outlined: true
                                    },
                                    acceptProps: {
                                        label: 'Sim'
                                    },
                                    accept: () => {
                                        this.$router.push(`/cadastrar-curriculo/${numericValue}`);
                                    },
                                    reject: () => {
                                        this.value = null;
                                        this.value_aux = null;
                                        this.$toast.add({ severity: 'warn', summary: 'Cancelado', detail: 'Você optou por não cadastrar um novo currículo', life: 3000 });
                                    }
                                });
                            });
                    }
                }
            }
        },
        editCurriculo() {
            this.$router.push(`/cadastrar-curriculo/${this.curriculo.cpf}`);
        },
        hideDialog() {
            this.value = null
            this.visible = false
            this.value_aux = null
        }

    },
    mounted() {
        api.getStores()
            .then(response => {
                this.lojas = response.data;
                this.loadingLojas = false;
            })
            .catch(error => {
                handleStoreErrors(error, this.$router, this.$toast)
            });

        api.getDepartments()
            .then(response => {
                this.setores = response.data;
                this.loadingSetores = false;
            })
            .catch(error => {
                handleDepartmentErrors(error, this.$router, this.$toast)
            });
    }
}
</script>
