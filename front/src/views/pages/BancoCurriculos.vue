<template>
    <div class="card">
        <DataTable removableSort sortMode="multiple" :reorderableColumns="true" v-model:filters="filters"
            :value="curriculos" paginator :loading="loading" :rows="5" :rowsPerPageOptions="[5, 10, 20, 50]"
            filterDisplay="menu" :globalFilterFields="globalFilterFields" tableStyle="min-width: 50rem">
            <template #header>
                <div class="flex flex-wrap justify-between">
                    <Button type="button" icon="pi pi-filter-slash" label="Remover Filtro" outlined
                        @click="clearFilter()" />
                    <div class="flex flex-wrap gap-2">
                        <MultiSelect v-model="selectedColumns" selectedItemsLabel="{0} Colunas Selecionadas"
                            maxSelectedLabels="1" :options="columns" optionLabel="header" filter :showToggleAll="false"
                            @update:modelValue="onToggle" placeholder="Selecionar Colunas" style="width: 18rem;" />
                        <IconField>
                            <InputIcon>
                                <i class="pi pi-search" />
                            </InputIcon>
                            <InputText v-model="filters['global'].value" placeholder="Procurar" />
                        </IconField>
                    </div>
                </div>
            </template>
            <template #empty> Nenhum currículo encontrado. </template>
            <template #loading> Carregando Currículos. Por favor aguarde. </template>
            <Column v-if="selectedColumns.some(col => col.field === 'nome')" field="nome" header="Nome"
                maxConstraints="99" sortable style="min-width: 20rem;">
                <template #body="{ data }">
                    <span> {{ formatNome(data.nome) }}</span>
                </template>
                <template #filter="{ filterModel }">
                    <InputText v-model="filterModel.value" type="text" placeholder="Procurar por nome" />
                </template>
            </Column>


            <Column v-if="selectedColumns.some(col => col.field === 'foto')" field="foto" header="Foto"
                maxConstraints="99">
                <template #body="{ data }">
                    <Avatar v-if="!data.foto" icon="pi pi-user" size="large" shape="circle" />
                    <Image v-else alt="Image" preview>
                        <template #image>
                            <Avatar :image="'http://127.0.0.1:8000/' + data.foto.foto" size="large" shape="circle" />
                        </template>
                        <template #preview="slotProps">
                            <img :src="'http://127.0.0.1:8000/' + data.foto.foto" alt="preview" :style="slotProps.style"
                                @click="slotProps.onClick" />
                        </template>
                    </Image>
                </template>
            </Column>

            <Column v-if="selectedColumns.some(col => col.field === 'idade')" field="idade" dataType="numeric"
                header="Idade" maxConstraints="99" sortable>
                <template #body="{ data }">
                    <span>{{ data.idade }}</span>
                </template>
                <template #filter="{ filterModel }">
                    <InputNumber v-model="filterModel.value" :useGrouping="false" placeholder="Procurar por idade" />
                </template>
            </Column>

            <Column v-if="selectedColumns.some(col => col.field === 'cpf')" field="cpf" header="CPF" maxConstraints="99"
                sortable style="min-width: 12rem;">
                <template #body="{ data }">
                    <span>{{ formatCPF(data.cpf) }}</span>
                </template>
                <template #filter="{ filterModel }">
                    <InputNumber v-model="filterModel.value" :useGrouping="false" placeholder="Procurar por CPF" />
                </template>
            </Column>

            <Column v-if="selectedColumns.some(col => col.field === 'rg')" field="rg" header="RG" maxConstraints="99"
                sortable style="min-width: 12rem;">
                <template #body="{ data }">
                    <span>{{ formatRG(data.rg) }}</span>
                </template>
                <template #filter="{ filterModel }">
                    <InputNumber v-model="filterModel.value" :useGrouping="false" placeholder="Procurar por RG" />
                </template>
            </Column>

            <Column v-if="selectedColumns.some(col => col.field === 'telefone')" field="telefone" header="Telefone 1"
                maxConstraints="99" sortable style="min-width: 14rem;">
                <template #body="{ data }">
                    <span>{{ formatPhone(data.telefone) }}</span>
                </template>
                <template #filter="{ filterModel }">
                    <InputNumber v-model="filterModel.value" :useGrouping="false" placeholder="Procurar por telefone" />
                </template>
            </Column>

            <Column v-if="selectedColumns.some(col => col.field === 'telefone_adicional')" field="telefone_adicional"
                header="Telefone 2" maxConstraints="99" sortable style="min-width: 14rem;">
                <template #body="{ data }">
                    <span>{{ formatPhone(data.telefone_adicional) }}</span>
                </template>
                <template #filter="{ filterModel }">
                    <InputNumber v-model="filterModel.value" :useGrouping="false" placeholder="Procurar por telefone" />
                </template>
            </Column>

            <Column v-if="selectedColumns.some(col => col.field === 'data_de_nascimento')" field="data_de_nascimento"
                dataType="date" header="Data de nascimento" maxConstraints="99" sortable style="min-width: 20rem;">
                <template #body="{ data }">
                    {{ formatDate(data.data_de_nascimento) }}
                </template>
                <template #filter="{ filterModel }">
                    <DatePicker id="datepicker" fluid v-model="filterModel.value" placeholder="Procurar por data" />
                </template>
            </Column>

            <Column v-if="selectedColumns.some(col => col.field === 'estado_civil')" field="estado_civil"
                header="Estado Civil" maxConstraints="99" sortable :showFilterMatchModes="false"
                style="min-width: 20rem;">
                <template #body="{ data }">
                    <span>{{ data.estado_civil }}</span>
                </template>
                <template #filter="{ filterModel }">
                    <Select v-model="filterModel.value" :options="estado_civil" filter fluid
                        placeholder="Procurar por estado civil" showClear />
                </template>
            </Column>

            <Column v-if="selectedColumns.some(col => col.field === 'escolaridade')" field="escolaridade"
                header="Escolaridade" maxConstraints="99" sortable :showFilterMatchModes="false"
                style="min-width: 20rem;">
                <template #body="{ data }">
                    <span>{{ data.escolaridade }}</span>
                </template>
                <template #filter="{ filterModel }">
                    <Select v-model="filterModel.value" :options="escolaridade" filter fluid
                        placeholder="Procurar por escolaridade" showClear />
                </template>
            </Column>

            <Column v-if="selectedColumns.some(col => col.field === 'possui_cursos_complementares')"
                field="possui_cursos_complementares" dataType="boolean" header="Possui Cursos Complementares"
                maxConstraints="99" sortable>
                <template #body="{ data }">
                    <Tag v-if="!data.possui_cursos_complementares" value="Não" />
                    <Tag v-else severity="contrast" value="Sim" />
                </template>
                <template #filter="{ filterModel }">
                    <Select v-model="filterModel.value" :options="[true, false]" placeholder="Selecione Sim/Não"
                        showClear>
                        <template #value="slotProps">
                            <Tag v-if="slotProps.value == false" value="Não" />
                            <Tag v-if="slotProps.value == true" severity="contrast" value="Sim" />
                        </template>
                        <template #option="slotProps">
                            <Tag v-if="slotProps.option == false" value="Não" />
                            <Tag v-if="slotProps.option == true" severity="contrast" value="Sim" />
                        </template>
                    </Select>
                </template>
            </Column>

            <Column v-if="selectedColumns.some(col => col.field === 'cursos_observacao')" field="cursos_observacao"
                header="Observações (Cursos)" maxConstraints="99" sortable style="min-width: 20rem;">
                <template #body="{ data }">
                    <span>{{ formatString(data.cursos_observacao) }}</span>
                </template>
                <template #filter="{ filterModel }">
                    <InputText v-model="filterModel.value" type="text" placeholder="Procurar por observações" />
                </template>
            </Column>

            <Column v-if="selectedColumns.some(col => col.field === 'possui_dependentes')" field="possui_dependentes"
                dataType="boolean" header="Possui Dependentes" maxConstraints="99" sortable>
                <template #body="{ data }">
                    <Tag v-if="!data.possui_dependentes" value="Não" />
                    <Tag v-else severity="contrast" value="Sim" />
                </template>
                <template #filter="{ filterModel }">
                    <Select v-model="filterModel.value" :options="[true, false]" placeholder="Selecione Sim/Não"
                        showClear>
                        <template #value="slotProps">
                            <Tag v-if="slotProps.value == false" value="Não" />
                            <Tag v-if="slotProps.value == true" severity="contrast" value="Sim" />
                        </template>
                        <template #option="slotProps">
                            <Tag v-if="slotProps.option == false" value="Não" />
                            <Tag v-if="slotProps.option == true" severity="contrast" value="Sim" />
                        </template>
                    </Select>
                </template>
            </Column>

            <Column v-if="selectedColumns.some(col => col.field === 'numero_dependentes')" field="numero_dependentes"
                dataType="numeric" header="Nº Dependentes" maxConstraints="99" sortable>
                <template #body="{ data }">
                    <span>{{ data.numero_dependentes }}</span>
                </template>
                <template #filter="{ filterModel }">
                    <InputNumber v-model="filterModel.value" :useGrouping="false" placeholder="Nº dependentes" />
                </template>
            </Column>

            <Column v-if="selectedColumns.some(col => col.field === 'observacao_dependentes')"
                field="observacao_dependentes" header="Observações (Dependentes)" maxConstraints="99" sortable
                style="min-width: 20rem;">
                <template #body="{ data }">
                    <span>{{ formatString(data.observacao_dependentes) }}</span>
                </template>
                <template #filter="{ filterModel }">
                    <InputText v-model="filterModel.value" type="text" placeholder="Procurar por observações" />
                </template>
            </Column>

            <Column v-if="selectedColumns.some(col => col.field === 'cep')" field="cep" header="CEP" maxConstraints="99"
                sortable style="min-width: 20rem;">
                <template #body="{ data }">
                    <span>{{ formatCEP(data.cep) }}</span>
                </template>
                <template #filter="{ filterModel }">
                    <InputNumber v-model="filterModel.value" :useGrouping="false" placeholder="Procurar por cep" />
                </template>
            </Column>

            <Column v-if="selectedColumns.some(col => col.field === 'cidade')" field="cidade" header="Cidade"
                maxConstraints="99" sortable style="min-width: 20rem;">
                <template #body="{ data }">
                    <span>{{ formatNome(data.cidade) }}</span>
                </template>
                <template #filter="{ filterModel }">
                    <InputText v-model="filterModel.value" type="text" placeholder="Procurar por cidade" />
                </template>
            </Column>

            <Column v-if="selectedColumns.some(col => col.field === 'uf')" field="uf" header="Unidade Federativa"
                maxConstraints="99" sortable style="min-width: 20rem;">
                <template #body="{ data }">
                    <span>{{ formatNome(data.uf) }}</span>
                </template>
                <template #filter="{ filterModel }">
                    <Select v-model="filterModel.value" :options="ufs" placeholder="Procurar por UF" filter />
                </template>
            </Column>

            <Column v-if="selectedColumns.some(col => col.field === 'bairro')" field="bairro" header="Bairro"
                maxConstraints="99" sortable style="min-width: 20rem;">
                <template #body="{ data }">
                    <span>{{ formatNome(data.bairro) }}</span>
                </template>
                <template #filter="{ filterModel }">
                    <InputText v-model="filterModel.value" type="text" placeholder="Procurar por bairro" />
                </template>
            </Column>

            <Column v-if="selectedColumns.some(col => col.field === 'rua')" field="rua" header="Rua" maxConstraints="99"
                sortable style="min-width: 20rem;">
                <template #body="{ data }">
                    <span>{{ formatNome(data.rua) }}</span>
                </template>
                <template #filter="{ filterModel }">
                    <InputText v-model="filterModel.value" type="text" placeholder="Procurar por rua" />
                </template>
            </Column>

            <Column v-if="selectedColumns.some(col => col.field === 'numero')" field="numero" header="Nº"
                maxConstraints="99" sortable>
                <template #body="{ data }">
                    <span>{{ data.numero }}</span>
                </template>
                <template #filter="{ filterModel }">
                    <InputNumber v-model="filterModel.value" placeholder="Procurar por número" />
                </template>
            </Column>

            <Column v-if="selectedColumns.some(col => col.field === 'complemento')" field="complemento"
                header="Complemento" maxConstraints="99" sortable style="min-width: 20rem;">
                <template #body="{ data }">
                    <span>{{ formatString(data.complemento) }}</span>
                </template>
                <template #filter="{ filterModel }">
                    <InputText v-model="filterModel.value" type="text" placeholder="Procurar por complemento" />
                </template>
            </Column>

            <Column v-if="selectedColumns.some(col => col.field === 'apresentacao_curriculo')"
                field="apresentacao_curriculo" dataType="numeric" header="Apresentação Currículo" maxConstraints="99"
                sortable>
                <template #body="{ data }">
                    <Rating v-model="data.apresentacao_curriculo" readonly />
                </template>
                <template #filter="{ filterModel }">
                    <div class="flex p-2 justify-center">
                        <Rating v-model="filterModel.value"
                            @change="() => { if (!filterModel.value) filterModel.value = 0 }" />

                    </div>
                </template>
            </Column>

            <Column v-if="selectedColumns.some(col => col.field === 'apresentacao_pessoal')"
                field="apresentacao_pessoal" dataType="numeric" header="Apresentação Pessoal" maxConstraints="99"
                sortable>
                <template #body="{ data }">
                    <Rating v-model="data.apresentacao_pessoal" readonly />
                </template>
                <template #filter="{ filterModel }">
                    <div class="flex p-2 justify-center">
                        <Rating v-model="filterModel.value"
                            @change="() => { if (!filterModel.value) filterModel.value = 0 }" />
                    </div>
                </template>
            </Column>

            <Column v-if="selectedColumns.some(col => col.field === 'apresentacao_observacao')"
                field="apresentacao_observacao" header="Observações (Apresentação)" maxConstraints="99" sortable
                style="min-width: 20rem;">
                <template #body="{ data }">
                    <span>{{ formatString(data.apresentacao_observacao) }}</span>
                </template>
                <template #filter="{ filterModel }">
                    <InputText v-model="filterModel.value" type="text" placeholder="Procurar por observações" />
                </template>
            </Column>

            <Column v-if="selectedColumns.some(col => col.field === 'possui_experiencia')" field="possui_experiencia"
                dataType="boolean" header="Possui Experiência" maxConstraints="99" sortable>
                <template #body="{ data }">
                    <Tag v-if="!data.possui_experiencia" value="Não" />
                    <Tag v-else severity="contrast" value="Sim" />
                </template>
                <template #filter="{ filterModel }">
                    <Select v-model="filterModel.value" :options="[true, false]" placeholder="Selecione Sim/Não"
                        showClear>
                        <template #value="slotProps">
                            <Tag v-if="slotProps.value == false" value="Não" />
                            <Tag v-if="slotProps.value == true" severity="contrast" value="Sim" />
                        </template>
                        <template #option="slotProps">
                            <Tag v-if="slotProps.option == false" value="Não" />
                            <Tag v-if="slotProps.option == true" severity="contrast" value="Sim" />
                        </template>
                    </Select>
                </template>
            </Column>

            <Column v-if="selectedColumns.some(col => col.field === 'relato_experiencia')" field="relato_experiencia"
                dataType="numeric" header="Relato Experiência" maxConstraints="99" sortable>
                <template #body="{ data }">
                    <Rating v-model="data.relato_experiencia" readonly />
                </template>
                <template #filter="{ filterModel }">
                    <div class="flex p-2 justify-center">
                        <Rating v-model="filterModel.value"
                            @change="() => { if (!filterModel.value) filterModel.value = 0 }" />
                    </div>
                </template>
            </Column>

            <Column v-if="selectedColumns.some(col => col.field === 'relato_desligamento')" field="relato_desligamento"
                dataType="numeric" header="Relato Desligamento" maxConstraints="99" sortable>
                <template #body="{ data }">
                    <Rating v-model="data.relato_desligamento" readonly />
                </template>
                <template #filter="{ filterModel }">
                    <div class="flex p-2 justify-center">
                        <Rating v-model="filterModel.value"
                            @change="() => { if (!filterModel.value) filterModel.value = 0 }" />
                    </div>
                </template>
            </Column>

            <Column v-if="selectedColumns.some(col => col.field === 'observacao_experiencia')"
                field="observacao_experiencia" header="Observações (Experiência)" maxConstraints="99" sortable
                style="min-width: 20rem;">
                <template #body="{ data }">
                    <span>{{ formatString(data.observacao_experiencia) }}</span>
                </template>
                <template #filter="{ filterModel }">
                    <InputText v-model="filterModel.value" type="text" placeholder="Procurar por observações" />
                </template>
            </Column>

            <Column v-if="selectedColumns.some(col => col.field === 'relato_motivacao')" field="relato_motivacao"
                dataType="numeric" header="Relato Motivação" maxConstraints="99" sortable>
                <template #body="{ data }">
                    <Rating v-model="data.relato_motivacao" readonly />
                </template>
                <template #filter="{ filterModel }">
                    <div class="flex p-2 justify-center">
                        <Rating v-model="filterModel.value"
                            @change="() => { if (!filterModel.value) filterModel.value = 0 }" />
                    </div>
                </template>
            </Column>

            <Column v-if="selectedColumns.some(col => col.field === 'lojas_interesse')" field="lojas_interesse_aux"
                header="Lojas Interesse" maxConstraints="99" sortable :showFilterMatchModes="false"
                style="min-width: 20rem;">
                <template #body="{ data }">
                    <div class="flex flex-wrap gap-1">
                        <Tag v-for="loja in data.lojas_interesse" :key="loja" :severity="loja.color"
                            :value="loja.name" />
                    </div>
                </template>
                <template #filter="{ filterModel }">
                    <Select v-model="filterModel.value" :options="lojas" optionValue="json" optionLabel="name" filter
                        placeholder="Selecione uma Loja" showClear>
                        <template #value="slotProps">
                            <Tag v-if="slotProps.value" :key="slotProps.value"
                                :severity="JSON.parse(slotProps.value).color"
                                :value="JSON.parse(slotProps.value).name" />
                        </template>
                        <template #option="slotProps">
                            <Tag :key="slotProps.option" :severity="slotProps.option.color"
                                :value="slotProps.option.name" />
                        </template>
                    </Select>
                </template>
            </Column>

            <Column v-if="selectedColumns.some(col => col.field === 'setores_interesse')" field="setores_interesse_aux"
                header="Setores Interesse" maxConstraints="99" sortable :showFilterMatchModes="false"
                style="min-width: 20rem;">
                <template #body="{ data }">
                    <div class="flex flex-wrap gap-1">
                        <Tag v-for="setor in data.setores_interesse" :key="setor" :severity="setor.color"
                            :value="setor.name" />
                    </div>
                </template>
                <template #filter="{ filterModel }">
                    <Select v-model="filterModel.value" :options="setores" optionValue="json" optionLabel="name" filter
                        placeholder="Selecione um Setor" showClear>
                        <template #value="slotProps">
                            <Tag v-if="slotProps.value" :key="slotProps.value"
                                :severity="JSON.parse(slotProps.value).color"
                                :value="JSON.parse(slotProps.value).name" />
                        </template>
                        <template #option="slotProps">
                            <Tag :key="slotProps.option" :severity="slotProps.option.color"
                                :value="slotProps.option.name" />
                        </template>
                    </Select>
                </template>
            </Column>

            <Column v-if="selectedColumns.some(col => col.field === 'relato_interesse')" field="relato_interesse"
                dataType="numeric" header="Relato Interesse" maxConstraints="99" sortable>
                <template #body="{ data }">
                    <Rating v-model="data.relato_interesse" readonly />
                </template>
                <template #filter="{ filterModel }">
                    <div class="flex p-2 justify-center">
                        <Rating v-model="filterModel.value"
                            @change="() => { if (!filterModel.value) filterModel.value = 0 }" />
                    </div>
                </template>
            </Column>

            <Column v-if="selectedColumns.some(col => col.field === 'relato_equipe')" field="relato_equipe"
                dataType="numeric" header="Relato Equipe" maxConstraints="99" sortable>
                <template #body="{ data }">
                    <Rating v-model="data.relato_equipe" readonly />
                </template>
                <template #filter="{ filterModel }">
                    <div class="flex p-2 justify-center">
                        <Rating v-model="filterModel.value"
                            @change="() => { if (!filterModel.value) filterModel.value = 0 }" />
                    </div>
                </template>
            </Column>

            <Column v-if="selectedColumns.some(col => col.field === 'restricoes_horario')" field="restricoes_horario"
                dataType="boolean" header="Possui Restrições Horário" maxConstraints="99" sortable>
                <template #body="{ data }">
                    <Tag v-if="!data.restricoes_horario" value="Não" />
                    <Tag v-else severity="contrast" value="Sim" />
                </template>
                <template #filter="{ filterModel }">
                    <Select v-model="filterModel.value" :options="[true, false]" placeholder="Selecione Sim/Não"
                        showClear>
                        <template #value="slotProps">
                            <Tag v-if="slotProps.value == false" value="Não" />
                            <Tag v-if="slotProps.value == true" severity="contrast" value="Sim" />
                        </template>
                        <template #option="slotProps">
                            <Tag v-if="slotProps.option == false" value="Não" />
                            <Tag v-if="slotProps.option == true" severity="contrast" value="Sim" />
                        </template>
                    </Select>
                </template>
            </Column>

            <Column v-if="selectedColumns.some(col => col.field === 'observacoes_entrevista')"
                field="observacoes_entrevista" header="Observações (Entrevista)" maxConstraints="99" sortable
                style="min-width: 20rem;">
                <template #body="{ data }">
                    <span>{{ formatString(data.observacoes_entrevista) }}</span>
                </template>
                <template #filter="{ filterModel }">
                    <InputText v-model="filterModel.value" type="text" placeholder="Procurar por observações" />
                </template>
            </Column>

            <Column v-if="selectedColumns.some(col => col.field === 'entrevistador')" field="entrevistador"
                header="Entrevistador" maxConstraints="99" sortable style="min-width: 20rem;">
                <template #body="{ data }">
                    <span>{{ formatNome(data.entrevistador) }}</span>
                </template>
                <template #filter="{ filterModel }">
                    <InputText v-model="filterModel.value" type="text" placeholder="Procurar por entrevistador" />
                </template>
            </Column>

            <Column v-if="selectedColumns.some(col => col.field === 'setores_ideal')" field="setores_ideal_aux"
                header="Setores Ideais" maxConstraints="99" sortable :showFilterMatchModes="false"
                style="min-width: 20rem;">
                <template #body="{ data }">
                    <div class="flex flex-wrap gap-1">
                        <Tag v-for="setor in data.setores_ideal" :key="setor" :severity="setor.color"
                            :value="setor.name" />
                    </div>
                </template>
                <template #filter="{ filterModel }">
                    <Select v-model="filterModel.value" :options="setores" optionValue="json" optionLabel="name" filter
                        placeholder="Selecione um Setor" showClear>
                        <template #value="slotProps">
                            <Tag v-if="slotProps.value" :key="slotProps.value"
                                :severity="JSON.parse(slotProps.value).color"
                                :value="JSON.parse(slotProps.value).name" />
                        </template>
                        <template #option="slotProps">
                            <Tag :key="slotProps.option" :severity="slotProps.option.color"
                                :value="slotProps.option.name" />
                        </template>
                    </Select>
                </template>
            </Column>

            <Column v-if="selectedColumns.some(col => col.field === 'bate_perfil_setor')" field="bate_perfil_setor"
                dataType="boolean" header="Perfil Ideal" maxConstraints="99" sortable>
                <template #body="{ data }">
                    <Tag v-if="!data.bate_perfil_setor" value="Não" />
                    <Tag v-else severity="contrast" value="Sim" />
                </template>
                <template #filter="{ filterModel }">
                    <Select v-model="filterModel.value" :options="[true, false]" placeholder="Selecione Sim/Não"
                        showClear>
                        <template #value="slotProps">
                            <Tag v-if="slotProps.value == false" value="Não" />
                            <Tag v-if="slotProps.value == true" severity="contrast" value="Sim" />
                        </template>
                        <template #option="slotProps">
                            <Tag v-if="slotProps.option == false" value="Não" />
                            <Tag v-if="slotProps.option == true" severity="contrast" value="Sim" />
                        </template>
                    </Select>
                </template>
            </Column>

            <Column v-if="selectedColumns.some(col => col.field === 'apto_contratacao')" field="apto_contratacao"
                dataType="boolean" header="Apto" maxConstraints="99" sortable>
                <template #body="{ data }">
                    <Tag v-if="!data.apto_contratacao" value="Não" />
                    <Tag v-else severity="contrast" value="Sim" />
                </template>
                <template #filter="{ filterModel }">
                    <Select v-model="filterModel.value" :options="[true, false]" placeholder="Selecione Sim/Não"
                        showClear>
                        <template #value="slotProps">
                            <Tag v-if="slotProps.value == false" value="Não" />
                            <Tag v-if="slotProps.value == true" severity="contrast" value="Sim" />
                        </template>
                        <template #option="slotProps">
                            <Tag v-if="slotProps.option == false" value="Não" />
                            <Tag v-if="slotProps.option == true" severity="contrast" value="Sim" />
                        </template>
                    </Select>
                </template>
            </Column>

            <Column v-if="selectedColumns.some(col => col.field === 'ex_funcionario')" field="ex_funcionario"
                dataType="boolean" header="Ex-Funcionário" maxConstraints="99" sortable>
                <template #body="{ data }">
                    <Tag v-if="!data.ex_funcionario" value="Não" />
                    <Tag v-else severity="contrast" value="Sim" />
                </template>
                <template #filter="{ filterModel }">
                    <Select v-model="filterModel.value" :options="[true, false]" placeholder="Selecione Sim/Não"
                        showClear>
                        <template #value="slotProps">
                            <Tag v-if="slotProps.value == false" value="Não" />
                            <Tag v-if="slotProps.value == true" severity="contrast" value="Sim" />
                        </template>
                        <template #option="slotProps">
                            <Tag v-if="slotProps.option == false" value="Não" />
                            <Tag v-if="slotProps.option == true" severity="contrast" value="Sim" />
                        </template>
                    </Select>
                </template>
            </Column>

            <Column v-if="selectedColumns.some(col => col.field === 'atualmente_contratado')" dataType="boolean"
                field="atualmente_contratado" header="Atualmente Contratado" maxConstraints="99" sortable>
                <template #body="{ data }">
                    <Tag v-if="!data.atualmente_contratado" value="Não" />
                    <Tag v-else severity="contrast" value="Sim" />
                </template>
                <template #filter="{ filterModel }">
                    <Select v-model="filterModel.value" :options="[true, false]" placeholder="Selecione Sim/Não"
                        showClear>
                        <template #value="slotProps">
                            <Tag v-if="slotProps.value == false" value="Não" />
                            <Tag v-if="slotProps.value == true" severity="contrast" value="Sim" />
                        </template>
                        <template #option="slotProps">
                            <Tag v-if="slotProps.option == false" value="Não" />
                            <Tag v-if="slotProps.option == true" severity="contrast" value="Sim" />
                        </template>
                    </Select>
                </template>
            </Column>

            <Column v-if="selectedColumns.some(col => col.field === 'observacao')" field="observacao"
                header="Observações" maxConstraints="99" sortable style="min-width: 20rem;">
                <template #body="{ data }">
                    <span>{{ formatString(data.observacao) }}</span>
                </template>
                <template #filter="{ filterModel }">
                    <InputText v-model="filterModel.value" type="text" placeholder="Procurar por observações" />
                </template>
            </Column>

            <Column v-if="selectedColumns.some(col => col.field === 'ultima_atualizacao')" field="ultima_atualizacao"
                dataType="date" header="Última Atualização" maxConstraints="99" sortable style="min-width: 20rem;">
                <template #body="{ data }">
                    <Tag :value="formatDateTime(data.ultima_atualizacao)"
                        :severity="getSeverityDate(data.ultima_atualizacao)" />
                </template>
                <template #filter="{ filterModel }">
                    <DatePicker id="datepicker-24h" showTime hourFormat="24" fluid v-model="filterModel.value"
                        placeholder="Procurar por data" />
                </template>
            </Column>

            <Column v-if="selectedColumns.some(col => col.field === 'curriculo')" field="curriculo" header="Currículo"
                maxConstraints="99">
                <template #body="{ data }">
                    <Avatar v-if="!data.curriculo" icon="pi pi-file-pdf" size="large" shape="circle" />
                    <Image v-else alt="Image" preview>
                        <template #image>
                            <Avatar :image="'http://127.0.0.1:8000/' + data.curriculo.foto" size="large"
                                shape="circle" />
                        </template>
                        <template #preview="slotProps">
                            <img :src="'http://127.0.0.1:8000/' + data.curriculo.foto" alt="preview"
                                :style="slotProps.style" @click="slotProps.onClick" />
                        </template>
                    </Image>
                </template>
            </Column>

            <Column v-if="selectedColumns.some(col => col.field === 'acoes')" field="acoes" style="min-width: 13rem;">
                <template #header="slotProps">
                    <div class="flex flex-wrap justify-end w-full">
                        <Button icon="pi pi-search" label="Consultar CPF" @click="addCurriculo" />
                    </div>
                </template>
                <template #body="slotProps">
                    <div class="flex justify-end">
                        <Button @click="viewCurriculo(slotProps.data)" icon="pi pi-eye" severity="info" text
                            aria-label="View" />
                        <Button @click="editCurriculo(slotProps.data)" icon="pi pi-pencil" text aria-label="Edit" />
                        <Button @click="deleteCurriculo(slotProps.data)" icon="pi pi-trash" severity="danger" text
                            aria-label="Delete" />
                    </div>
                </template>
            </Column>
        </DataTable>

    </div>
    <Dialog v-if="curriculo" v-model:visible="visible" modal :style="{ width: '50rem' }"
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
                        <InputMask readonly v-model="curriculo.rg" mask="9999?9999-99" placeholder="99999999-99"
                            fluid />
                        <label>RG</label>
                    </FloatLabel>
                </div>
            </div>
            <div class="flex flex-row flex-wrap gap-3">
                <div class="flex-1">
                    <div class="flex flex-col mb-6">
                        <FloatLabel>
                            <InputMask readonly v-model="curriculo.telefone" mask="(99) 9999-9999?9"
                                placeholder="(99) 9999-99999" fluid />
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
import { FilterMatchMode, FilterOperator } from '@primevue/core/api';
import { useRouter } from 'vue-router';
import { handleStoreErrors, handleDepartmentErrors, handleCurriculoErrors } from '@/common/utils';
import { api } from '@/service/api';
import InputNumber from 'primevue/inputnumber';

export default {
    data() {
        return {
            router: useRouter(),
            curriculos: null,
            curriculo: null,
            visible: false,
            roles: [
                'rh',
                'admin'
            ],
            filters: null,
            loading: false,
            lojas: [],
            setores: [],
            editor: {},
            selectedColumns: null,
            columns: null,
            globalFilterFields: [
                'nome',
                'foto',
                'curriculo',
                'idade',
                'cpf',
                'rg',
                'telefone',
                'telefone_adicional',
                'data_de_nascimento',
                'estado_civil',
                'escolaridade',
                'possui_cursos_complementares',
                'cursos_observacao',
                'possui_dependentes',
                'numero_dependentes',
                'observacao_dependentes',
                'cep',
                'cidade',
                'uf',
                'bairro',
                'rua',
                'numero',
                'complemento',
                'apresentacao_curriculo',
                'apresentacao_pessoal',
                'apresentacao_observacao',
                'possui_experiencia',
                'relato_experiencia',
                'relato_desligamento',
                'observacao_experiencia',
                'relato_motivacao',
                'lojas_interesse_aux',
                'setores_interesse_aux',
                'bate_perfil_setor',
                'relato_interesse',
                'relato_equipe',
                'restricoes_horario',
                'observacoes_entrevista',
                'entrevistador',
                'setores_ideal_aux',
                'apto_contratacao',
                'ex_funcionario',
                'atualmente_contratado',
                'observacao',
                'ultima_atualizacao',
                'acoes'
            ],
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
        };
    },
    methods: {
        onToggle(value) { },
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
        formatDate(input) {
            if (!input) return input;

            if (!(input instanceof Date) || isNaN(input)) {
                return input;
            }

            const day = String(input.getDate()).padStart(2, '0');
            const month = String(input.getMonth() + 1).padStart(2, '0');
            const year = input.getFullYear();

            const formattedDate = `${day}/${month}/${year}`;
            return formattedDate;
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
        formatCPF(input) {
            if (!input) return input;

            let numericStr = input.replace(/\D/g, '');

            if (numericStr.length < 11) {
                return input;
            }

            numericStr = numericStr.substring(0, 11);

            const formattedCPF = `${numericStr.slice(0, 3)}.${numericStr.slice(3, 6)}.${numericStr.slice(6, 9)}-${numericStr.slice(9, 11)}`;

            return formattedCPF;
        },
        formatRG(input) {
            if (!input) return input;

            let numericStr = input.replace(/\D/g, '');

            if (numericStr.length < 9) {
                return numericStr.replace(/\B(?=(\d{3})+(?!\d))/g, ".");
            }

            numericStr = numericStr.substring(0, 9);

            const formattedRG = `${numericStr.slice(0, 2)}.${numericStr.slice(2, 5)}.${numericStr.slice(5, 8)}-${numericStr.slice(8, 9)}`;

            return formattedRG;
        },
        formatString(input) {
            if (!input) return input;

            if (input.length > 30) {
                input = input.substring(0, 26) + "...";
            }

            return input;
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
        formatPhone(input) {
            let numericStr = input.replace(/\D/g, '');

            if (numericStr.length < 10) {
                numericStr = numericStr.padStart(10, '0');
            }

            numericStr = numericStr.substring(0, 11);

            const ddd = numericStr.slice(0, 2);
            const firstPart = numericStr.length === 10 ? numericStr.slice(2, 6) : numericStr.slice(2, 7);
            const secondPart = numericStr.length === 10 ? numericStr.slice(6, 10) : numericStr.slice(7, 11);

            const formattedPhone = `(${ddd}) ${firstPart}-${secondPart}`;

            return formattedPhone;
        },
        formatCEP(input) {
            if (!input) return input;

            let numericStr = input.replace(/\D/g, '');

            if (numericStr.length < 8) {
                return input;
            }

            numericStr = numericStr.substring(0, 8);

            const formattedCEP = `${numericStr.slice(0, 5)}-${numericStr.slice(5, 9)}`;

            return formattedCEP;
        },
        clearCurriculos() {
            this.loading = true;

            api.getCurriculosCompleto()
                .then(response => {
                    console.log(response)
                    this.curriculos = response.data;
                    this.curriculos.forEach(curriculo => {
                        curriculo.ultima_atualizacao = new Date(curriculo.ultima_atualizacao)
                        curriculo.data_de_nascimento = new Date(curriculo.data_de_nascimento)
                        curriculo.setores_interesse_aux = JSON.stringify(curriculo.setores_interesse)
                        curriculo.setores_ideal_aux = JSON.stringify(curriculo.setores_ideal)
                        curriculo.lojas_interesse_aux = JSON.stringify(curriculo.lojas_interesse)
                        curriculo.bate_perfil_setor = curriculo.setores_interesse.some(setorInteresse =>
                            curriculo.setores_ideal.some(setorIdeal =>
                                setorInteresse.id === setorIdeal.id
                            ))
                        curriculo.acoes = ""
                    });
                    api.getStores()
                        .then(response => {
                            this.lojas = response.data;
                            this.lojas.forEach(loja => {
                                loja.json = JSON.stringify(loja)
                            });
                            api.getDepartments()
                                .then(response => {
                                    this.setores = response.data;
                                    this.setores.forEach(setore => {
                                        setore.json = JSON.stringify(setore)
                                    });
                                    this.loading = false;
                                })
                                .catch(error => {
                                    handleDepartmentErrors(error, this.$router, this.$toast);
                                    this.loading = false;
                                });
                        })
                        .catch(error => {
                            handleStoreErrors(error, this.$router, this.$toast);
                            this.loading = false;
                        });
                    this.loading = false;
                })
                .catch(error => {
                    handleCurriculoErrors(error, this.$router, this.$toast);
                    this.loading = false;
                });
        },
        clearFilter() {
            this.filters = {
                global: { value: null, matchMode: FilterMatchMode.CONTAINS },
                nome: { operator: FilterOperator.AND, constraints: [{ value: null, matchMode: FilterMatchMode.STARTS_WITH }] },
                idade: { operator: FilterOperator.AND, constraints: [{ value: null, matchMode: FilterMatchMode.LESS_THAN_OR_EQUAL_TO }] },
                cpf: { operator: FilterOperator.AND, constraints: [{ value: null, matchMode: FilterMatchMode.STARTS_WITH }] },
                rg: { operator: FilterOperator.AND, constraints: [{ value: null, matchMode: FilterMatchMode.STARTS_WITH }] },
                telefone: { operator: FilterOperator.AND, constraints: [{ value: null, matchMode: FilterMatchMode.STARTS_WITH }] },
                telefone_adicional: { operator: FilterOperator.AND, constraints: [{ value: null, matchMode: FilterMatchMode.STARTS_WITH }] },
                data_de_nascimento: { operator: FilterOperator.AND, constraints: [{ value: null, matchMode: FilterMatchMode.DATE_AFTER }] },
                estado_civil: { operator: FilterOperator.OR, constraints: [{ value: null, matchMode: FilterMatchMode.EQUALS }] },
                escolaridade: { operator: FilterOperator.OR, constraints: [{ value: null, matchMode: FilterMatchMode.EQUALS }] },
                possui_cursos_complementares: { value: null, matchMode: FilterMatchMode.EQUALS },
                cursos_observacao: { operator: FilterOperator.AND, constraints: [{ value: null, matchMode: FilterMatchMode.STARTS_WITH }] },
                possui_dependentes: { value: null, matchMode: FilterMatchMode.EQUALS },
                numero_dependentes: { operator: FilterOperator.AND, constraints: [{ value: null, matchMode: FilterMatchMode.LESS_THAN_OR_EQUAL_TO }] },
                observacao_dependentes: { operator: FilterOperator.AND, constraints: [{ value: null, matchMode: FilterMatchMode.STARTS_WITH }] },
                cep: { operator: FilterOperator.AND, constraints: [{ value: null, matchMode: FilterMatchMode.STARTS_WITH }] },
                cidade: { operator: FilterOperator.AND, constraints: [{ value: null, matchMode: FilterMatchMode.STARTS_WITH }] },
                uf: { operator: FilterOperator.AND, constraints: [{ value: null, matchMode: FilterMatchMode.STARTS_WITH }] },
                bairro: { operator: FilterOperator.AND, constraints: [{ value: null, matchMode: FilterMatchMode.STARTS_WITH }] },
                rua: { operator: FilterOperator.AND, constraints: [{ value: null, matchMode: FilterMatchMode.STARTS_WITH }] },
                numero: { operator: FilterOperator.AND, constraints: [{ value: null, matchMode: FilterMatchMode.STARTS_WITH }] },
                complemento: { operator: FilterOperator.AND, constraints: [{ value: null, matchMode: FilterMatchMode.STARTS_WITH }] },
                apresentacao_curriculo: { operator: FilterOperator.AND, constraints: [{ value: null, matchMode: FilterMatchMode.GREATER_THAN_OR_EQUAL_TO }] },
                apresentacao_pessoal: { operator: FilterOperator.AND, constraints: [{ value: null, matchMode: FilterMatchMode.GREATER_THAN_OR_EQUAL_TO }] },
                apresentacao_observacao: { operator: FilterOperator.AND, constraints: [{ value: null, matchMode: FilterMatchMode.STARTS_WITH }] },
                possui_experiencia: { value: null, matchMode: FilterMatchMode.EQUALS },
                relato_experiencia: { operator: FilterOperator.AND, constraints: [{ value: null, matchMode: FilterMatchMode.GREATER_THAN_OR_EQUAL_TO }] },
                relato_desligamento: { operator: FilterOperator.AND, constraints: [{ value: null, matchMode: FilterMatchMode.GREATER_THAN_OR_EQUAL_TO }] },
                observacao_experiencia: { operator: FilterOperator.AND, constraints: [{ value: null, matchMode: FilterMatchMode.STARTS_WITH }] },
                relato_motivacao: { operator: FilterOperator.AND, constraints: [{ value: null, matchMode: FilterMatchMode.GREATER_THAN_OR_EQUAL_TO }] },
                lojas_interesse_aux: { operator: FilterOperator.OR, constraints: [{ value: null, matchMode: FilterMatchMode.CONTAINS }] },
                setores_interesse_aux: { operator: FilterOperator.OR, constraints: [{ value: null, matchMode: FilterMatchMode.CONTAINS }] },
                setores_ideal_aux: { operator: FilterOperator.OR, constraints: [{ value: null, matchMode: FilterMatchMode.CONTAINS }] },
                bate_perfil_setor: { value: null, matchMode: FilterMatchMode.EQUALS },
                relato_interesse: { operator: FilterOperator.AND, constraints: [{ value: null, matchMode: FilterMatchMode.GREATER_THAN_OR_EQUAL_TO }] },
                relato_equipe: { operator: FilterOperator.AND, constraints: [{ value: null, matchMode: FilterMatchMode.GREATER_THAN_OR_EQUAL_TO }] },
                restricoes_horario: { value: null, matchMode: FilterMatchMode.EQUALS },
                observacoes_entrevista: { operator: FilterOperator.AND, constraints: [{ value: null, matchMode: FilterMatchMode.STARTS_WITH }] },
                entrevistador: { operator: FilterOperator.AND, constraints: [{ value: null, matchMode: FilterMatchMode.STARTS_WITH }] },
                apto_contratacao: { value: null, matchMode: FilterMatchMode.EQUALS },
                ex_funcionario: { value: null, matchMode: FilterMatchMode.EQUALS },
                atualmente_contratado: { value: null, matchMode: FilterMatchMode.EQUALS },
                observacao: { operator: FilterOperator.AND, constraints: [{ value: null, matchMode: FilterMatchMode.STARTS_WITH }] },
                ultima_atualizacao: { operator: FilterOperator.AND, constraints: [{ value: null, matchMode: FilterMatchMode.DATE_AFTER }] },
                acoes: { value: null, matchMode: FilterMatchMode.EQUALS },
            };
            this.columns = [
                { field: 'nome', header: 'Nome' },
                { field: 'foto', header: 'Foto' },
                { field: 'idade', header: 'Idade' },
                { field: 'cpf', header: 'CPF' },
                { field: 'rg', header: 'RG' },
                { field: 'telefone', header: 'Telefone 1' },
                { field: 'telefone_adicional', header: 'Telefone 2' },
                { field: 'data_de_nascimento', header: 'Data de nascimento' },
                { field: 'estado_civil', header: 'Estado Civil' },
                { field: 'escolaridade', header: 'Escolaridade' },
                { field: 'possui_cursos_complementares', header: 'Possui Cursos Complementares' },
                { field: 'cursos_observacao', header: 'Observação (Cursos)' },
                { field: 'possui_dependentes', header: 'Possui Dependentes' },
                { field: 'numero_dependentes', header: 'Número de Dependentes' },
                { field: 'observacao_dependentes', header: 'Observação (Dependentes)' },
                { field: 'cep', header: 'CEP' },
                { field: 'cidade', header: 'Cidade' },
                { field: 'uf', header: 'UF' },
                { field: 'bairro', header: 'Bairro' },
                { field: 'rua', header: 'Rua' },
                { field: 'numero', header: 'Número' },
                { field: 'complemento', header: 'Complemento' },
                { field: 'apresentacao_curriculo', header: 'Apresentação Currículo' },
                { field: 'apresentacao_pessoal', header: 'Apresentação Pessoal' },
                { field: 'apresentacao_observacao', header: 'Apresentação Observação' },
                { field: 'possui_experiencia', header: 'Possui Experiência' },
                { field: 'relato_experiencia', header: 'Relato Experiência' },
                { field: 'relato_desligamento', header: 'Relato Desligamento' },
                { field: 'observacao_experiencia', header: 'Observação (Experiência)' },
                { field: 'relato_motivacao', header: 'Relato Motivação' },
                { field: 'lojas_interesse', header: 'Lojas Interesse' },
                { field: 'setores_interesse', header: 'Setores Interesse' },
                { field: 'bate_perfil_setor', header: 'Perfil Ideal' },
                { field: 'relato_interesse', header: 'Relato Interesse' },
                { field: 'relato_equipe', header: 'Relato Equipe' },
                { field: 'restricoes_horario', header: 'Restrições Horário' },
                { field: 'observacoes_entrevista', header: 'Observações (Entrevista)' },
                { field: 'entrevistador', header: 'Entrevistador' },
                { field: 'setores_ideal', header: 'Setores Ideais' },
                { field: 'apto_contratacao', header: 'Apto' },
                { field: 'ex_funcionario', header: 'Ex-Funcionário' },
                { field: 'atualmente_contratado', header: 'Atualmente Contratado' },
                { field: 'observacao', header: 'Observações' },
                { field: 'ultima_atualizacao', header: 'Última Atualização' },
                { field: 'curriculo', header: 'Currículo' },
                { field: 'acoes', header: 'Ações' },
            ];
            this.selectedColumns = this.columns;
        },
        viewCurriculo(curriculo) {
            this.curriculo = curriculo;
            this.curriculo.view_setores_ideal = this.curriculo.setores_ideal;
            this.curriculo.view_setores_ideal.forEach(setor => {
                setor.json = JSON.stringify(setor)
            })
            this.curriculo.view_lojas_interesse = this.curriculo.lojas_interesse;
            this.curriculo.view_lojas_interesse.forEach(loja => {
                loja.json = JSON.stringify(loja)
            })
            this.curriculo.view_setores_interesse = this.curriculo.setores_interesse;
            this.curriculo.view_setores_interesse.forEach(setor => {
                setor.json = JSON.stringify(setor)
            })
            this.visible = true;
        },
        addCurriculo() {
            this.$router.push(`/`);
        },
        editCurriculo(curriculo) {
            this.$router.push(`/cadastrar-curriculo/${curriculo.cpf}`);
        },
        deleteCurriculo(curriculo) {
            this.$confirm.require({
                message: `Você tem certeza de que deseja excluir o currículo de ${this.formatNome(curriculo.nome)} (CPF: ${this.formatCPF(curriculo.cpf)})?`,
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

                    api.deleteCurriculo(curriculo.cpf)
                        .then(() => {
                            this.clearCurriculos();
                        })
                        .catch(error => {
                            handleCurriculoErrors(error, this.$router, this.$toast);
                            this.loading = false;
                        });

                    this.$toast.add({ severity: 'info', summary: 'Exclusão Confirmada', detail: `Currículo de ${curriculo.nome} (CPF: ${curriculo.cpf}) excluído com sucesso`, life: 10000 });
                },
                reject: () => {
                    this.$toast.add({ severity: 'warn', summary: 'Ação Cancelada', detail: `Você desistiu da exclusão do currículo de ${curriculo.nome}`, life: 10000 });
                }
            });
        },
    },
    created() {
        this.clearFilter();
    },
    mounted() {
        this.clearCurriculos();
    }
}
</script>
