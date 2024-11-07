<template>

    <div class="card flex justify-center">
        <Stepper v-model:value="activeStep" class="basis-[45rem] max-w-full">
            <StepList>
                <Step v-slot="{ activateCallback, value, a11yAttrs }" asChild :value="1">
                    <div class="hidden md:flex flex flex-row flex-auto gap-2" v-bind="a11yAttrs.root">
                        <button class="bg-transparent border-0 inline-flex flex-col gap-2" @click="activateCallback"
                            v-bind="a11yAttrs.header">
                            <span :class="[
                                'rounded-full border-2 w-12 h-12 inline-flex items-center justify-center',
                                { 'bg-primary text-primary-contrast border-primary': value <= activeStep, 'border-surface-200 dark:border-surface-700': value > activeStep }
                            ]">
                                <i class="pi pi-bookmark" />
                            </span>
                        </button>
                        <Divider />
                    </div>
                </Step>
                <Step v-slot="{ activateCallback, value, a11yAttrs }" asChild :value="2">
                    <div class="hidden md:flex flex flex-row flex-auto gap-2 pl-2" v-bind="a11yAttrs.root">
                        <button class="bg-transparent border-0 inline-flex flex-col gap-2" @click="activateCallback"
                            v-bind="a11yAttrs.header">
                            <span :class="[
                                'rounded-full border-2 w-12 h-12 inline-flex items-center justify-center',
                                { 'bg-primary text-primary-contrast border-primary': value <= activeStep, 'border-surface-200 dark:border-surface-700': value > activeStep }
                            ]">
                                <i class="pi pi-user" />
                            </span>
                        </button>
                        <Divider />
                    </div>
                </Step>
                <Step v-slot="{ activateCallback, value, a11yAttrs }" asChild :value="3">
                    <div class="hidden md:flex flex flex-row flex-auto gap-2 pl-2" v-bind="a11yAttrs.root">
                        <button class="bg-transparent border-0 inline-flex flex-col gap-2" @click="activateCallback"
                            v-bind="a11yAttrs.header">
                            <span :class="[
                                'rounded-full border-2 w-12 h-12 inline-flex items-center justify-center',
                                { 'bg-primary text-primary-contrast border-primary': value <= activeStep, 'border-surface-200 dark:border-surface-700': value > activeStep }
                            ]">
                                <i class="pi pi-users" />
                            </span>
                        </button>
                        <Divider />
                    </div>
                </Step>
                <Step v-slot="{ activateCallback, value, a11yAttrs }" asChild :value="4">
                    <div class="hidden md:flex flex flex-row flex-auto gap-2  pl-2" v-bind="a11yAttrs.root">
                        <button class="bg-transparent border-0 inline-flex flex-col gap-2" @click="activateCallback"
                            v-bind="a11yAttrs.header">
                            <span :class="[
                                'rounded-full border-2 w-12 h-12 inline-flex items-center justify-center',
                                { 'bg-primary text-primary-contrast border-primary': value <= activeStep, 'border-surface-200 dark:border-surface-700': value > activeStep }
                            ]">
                                <i class="pi pi-map-marker" />
                            </span>
                        </button>
                        <Divider />
                    </div>
                </Step>
                <Step v-slot="{ activateCallback, value, a11yAttrs }" asChild :value="5">
                    <div class="hidden md:flex flex flex-row flex-auto gap-2 pl-2" v-bind="a11yAttrs.root">
                        <button class="bg-transparent border-0 inline-flex flex-col gap-2" @click="activateCallback"
                            v-bind="a11yAttrs.header">
                            <span :class="[
                                'rounded-full border-2 w-12 h-12 inline-flex items-center justify-center',
                                { 'bg-primary text-primary-contrast border-primary': value <= activeStep, 'border-surface-200 dark:border-surface-700': value > activeStep }
                            ]">
                                <i class="pi pi-briefcase" />
                            </span>
                        </button>
                        <Divider />
                    </div>
                </Step>
                <Step v-slot="{ activateCallback, value, a11yAttrs }" asChild :value="6">
                    <div class="hidden md:flex flex flex-row flex-auto gap-2 pl-2" v-bind="a11yAttrs.root">
                        <button class="bg-transparent border-0 inline-flex flex-col gap-2" @click="activateCallback"
                            v-bind="a11yAttrs.header">
                            <span :class="[
                                'rounded-full border-2 w-12 h-12 inline-flex items-center justify-center',
                                { 'bg-primary text-primary-contrast border-primary': value <= activeStep, 'border-surface-200 dark:border-surface-700': value > activeStep }
                            ]">
                                <i class="pi pi-comments" />
                            </span>
                        </button>
                        <Divider />
                    </div>
                </Step>
                <Step v-slot="{ activateCallback, value, a11yAttrs }" asChild :value="7">
                    <div class="hidden md:flex flex flex-row pl-2" v-bind="a11yAttrs.root">
                        <button class="bg-transparent border-0 inline-flex flex-col gap-2" @click="activateCallback"
                            v-bind="a11yAttrs.header">
                            <span :class="[
                                'rounded-full border-2 w-12 h-12 inline-flex items-center justify-center',
                                { 'bg-primary text-primary-contrast border-primary': value <= activeStep, 'border-surface-200 dark:border-surface-700': value > activeStep }
                            ]">
                                <i class="pi pi-star" />
                            </span>
                        </button>
                    </div>
                </Step>
            </StepList>
            <StepPanels>
                <StepPanel v-slot="{ activateCallback }" :value="1">
                    <div class="flex flex-col gap-2 mx-auto" style="min-height: 16rem; max-width: 40rem">
                        <div class="text-center mt-4 mb-4 text-xl font-semibold">Currículo e Apresentação Pessoal</div>
                        <div class="flex flex-col gap-2">
                            <label>Estado do Currículo (indique se há rasuras, amassados ou se a foto
                                está em más condições). *
                                <Tag severity="info"
                                    v-tooltip.bottom='`Avalie de 1 a 5 estrelas, onde 1 estrela representa "Não atende às expectativas" e 5 estrelas representa "Atende plenamente às expectativas".`'
                                    value="‎ ? ‎" rounded></Tag>
                            </label>
                            <div class="flex flex-col gap-2 mt-1 mb-1">
                                <div class="flex justify-end">
                                    <Rating v-model="form.apresentacao_curriculo.value" />
                                </div>
                                <div class="flex justify-end">
                                    <small v-if="form.apresentacao_curriculo.validation_error">Este campo é
                                        obrigatório.</small>
                                </div>
                            </div>
                        </div>
                        <div class="flex flex-col gap-2 mt-5">
                            <label>Apresentação Pessoal (incluindo higiene, cuidados com os dentes,
                                unhas, roupas limpas, etc.). *
                                <Tag severity="info"
                                    v-tooltip.bottom='`Avalie de 1 a 5 estrelas, onde 1 estrela representa "Não atende às expectativas" e 5 estrelas representa "Atende plenamente às expectativas".`'
                                    value="‎ ? ‎" rounded></Tag>
                            </label>
                            <div class="flex flex-col gap-2 mt-1 mb-1">
                                <div class="flex justify-end">
                                    <Rating v-model="form.apresentacao_pessoal.value" />
                                </div>
                                <div class="flex justify-end">
                                    <small v-if="form.apresentacao_pessoal.validation_error">Este campo é
                                        obrigatório.</small>
                                </div>
                            </div>
                            <FloatLabel>
                                <Textarea
                                    v-tooltip.bottom="'Se não tiver observações para inserir, você pode deixar este campo em branco.'"
                                    maxlength="450" v-model="form.apresentacao_observacao.value" fluid rows="5"
                                    cols="30" />
                                <label>Observações</label>
                            </FloatLabel>
                        </div>
                    </div>
                    <div class="flex pt-6 justify-end">
                        <Button label="Próximo" icon="pi pi-arrow-right" iconPos="right" @click="activateCallback(2)" />
                    </div>
                </StepPanel>
                <StepPanel v-slot="{ activateCallback }" :value="2">
                    <div class="flex flex-col gap-2 mx-auto" style="min-height: 16rem; max-width: 40rem">
                        <div class="text-center mt-0 md:mt-4 mb-2 text-xl font-semibold">Dados Pessoais</div>
                        <div class="flex flex-row flex-wrap gap-3 mb-5">
                            <div v-if="!form.foto.value" class="flex gap-1 flex-1">
                                <Avatar icon="pi pi-user" size="large" shape="circle" />
                                <Button text icon="pi pi-plus" label="Adicionar Foto"
                                    @click="$refs.file_foto.click()" />
                                <input style="display:none" type="file" ref="file_foto"
                                    @change="loadImage($event, 'foto')" accept="image/png, image/jpeg">
                            </div>
                            <div v-else class="flex gap-1 flex-1">
                                <Image alt="Image" preview>
                                    <template #image>
                                        <Avatar :image="form.foto.value.foto" size="large" shape="circle" />
                                    </template>
                                    <template #preview="slotProps">
                                        <img :src="form.foto.value.foto" alt="preview" :style="slotProps.style"
                                            @click="slotProps.onClick" />
                                    </template>
                                </Image>
                                <Button label="Remover Foto" icon="pi pi-times" text severity="danger"
                                    @click="form.foto.value = null" />
                            </div>
                            <div v-if="!form.curriculo.value" class="flex gap-1 flex-1">
                                <Avatar icon="pi pi-file-pdf" size="large" shape="circle" />
                                <Button text icon="pi pi-plus" label="Adicionar Currículo"
                                    @click="$refs.file_curriculo.click()" />
                                <input style="display:none" type="file" ref="file_curriculo"
                                    @change="loadImage($event, 'curriculo')" accept="image/png, image/jpeg">
                            </div>
                            <div v-else class="flex gap-1 flex-1">
                                <Image alt="Image" preview>
                                    <template #image>
                                        <Avatar :image="form.curriculo.value.foto" size="large" shape="circle" />
                                    </template>
                                    <template #preview="slotProps">
                                        <img :src="form.curriculo.value.foto" alt="preview" :style="slotProps.style"
                                            @click="slotProps.onClick" />
                                    </template>
                                </Image>
                                <Button label="Remover Currículo" icon="pi pi-times" text severity="danger"
                                    @click="form.curriculo.value = null" />
                            </div>
                        </div>
                        <div class="flex flex-row flex-wrap gap-3">
                            <div class="flex-1">
                                <div class="flex flex-col mb-5">
                                    <FloatLabel>
                                        <InputText maxlength="200" :invalid="form.nome.validation_error" fluid
                                            v-model="form.nome.value" />
                                        <label>Nome *</label>
                                    </FloatLabel>
                                    <small v-if="form.nome.validation_error">Este campo é obrigatório.</small>
                                </div>
                            </div>
                            <div class="flex-1">
                                <div class="flex flex-col mb-5">
                                    <FloatLabel>
                                        <InputNumber :invalid="form.idade.validation_error" v-model="form.idade.value"
                                            inputId="minmax" :min="0" :max="150" fluid />
                                        <label>Idade *</label>
                                    </FloatLabel>
                                    <small v-if="form.idade.validation_error">Este campo é obrigatório.</small>
                                </div>
                            </div>
                        </div>
                        <div class="flex flex-row flex-wrap gap-3">
                            <div class="flex-1">
                                <div class="flex flex-col mb-5">
                                    <FloatLabel>
                                        <InputText :invalid="form.cpf.validation_error" disabled
                                            v-model="form.cpf.value" fluid />
                                        <label>CPF *</label>
                                    </FloatLabel>
                                    <small v-if="form.cpf.validation_error">Este campo é obrigatório.</small>
                                </div>
                            </div>
                            <div class="flex-1">
                                <FloatLabel>
                                    <InputMask
                                        v-tooltip.bottom="'Se não tiver um RG para inserir, você pode deixar este campo em branco.'"
                                        v-model="form.rg.value" mask="9999?9999-99" placeholder="99999999-99" fluid />
                                    <label>RG</label>
                                </FloatLabel>
                            </div>
                        </div>
                        <div class="flex flex-row flex-wrap gap-3 mb-5">
                            <div class="flex-1">
                                <FloatLabel>
                                    <InputMask :invalid="form.telefone.validation_error" v-model="form.telefone.value"
                                        mask="(99) 9999-9999?9" placeholder="(99) 9999-99999" fluid />
                                    <label>Telefone 1 *</label>
                                </FloatLabel>
                                <small v-if="form.telefone.validation_error">Este campo é obrigatório.</small>
                            </div>
                            <div class="flex-1">
                                <FloatLabel>
                                    <InputMask :invalid="form.telefone_adicional.validation_error"
                                        v-model="form.telefone_adicional.value" mask="(99) 9999-9999?9"
                                        placeholder="(99) 9999-99999" fluid />
                                    <label>Telefone 2 *</label>
                                </FloatLabel>
                                <small v-if="form.telefone_adicional.validation_error">Este campo é obrigatório.</small>
                            </div>
                        </div>
                        <div class="flex flex-row flex-wrap gap-3">
                            <div class="flex-1 mb-5">
                                <FloatLabel>
                                    <DatePicker :invalid="form.data_de_nascimento.validation_error"
                                        style="min-width: 150px;" v-model="form.data_de_nascimento.value" showIcon fluid
                                        :showOnFocus="false" />
                                    <label>Data de nascimento *</label>
                                </FloatLabel>
                                <small v-if="form.data_de_nascimento.validation_error">Este campo é obrigatório.</small>
                            </div>
                            <div class="flex-1 mb-5">
                                <FloatLabel>
                                    <Select :invalid="form.estado_civil.validation_error"
                                        placeholder="Selecione uma opção" v-model="form.estado_civil.value"
                                        :options="estado_civil" filter fluid />
                                    <label>Estado Civil *</label>
                                </FloatLabel>
                                <small v-if="form.estado_civil.validation_error">Este campo é obrigatório.</small>
                            </div>
                        </div>
                        <div class="flex flex-row flex-wrap gap-3 mb-5">
                            <div class="flex-1">
                                <FloatLabel>
                                    <Select :invalid="form.escolaridade.validation_error"
                                        placeholder="Selecione uma opção" v-model="form.escolaridade.value"
                                        :options="escolaridade" filter fluid />
                                    <label>Escolaridade *</label>
                                </FloatLabel>
                                <small v-if="form.escolaridade.validation_error">Este campo é obrigatório.</small>
                            </div>
                            <div class="flex-1">
                                <ToggleButton class="w-full" v-model="form.possui_cursos_complementares.value"
                                    onLabel="Possui Cursos Complementares" offLabel="Não Possui Cursos Complementares"
                                    @change="changeCursosComplementares" />
                            </div>
                        </div>
                        <FloatLabel class="mb-5">
                            <Textarea maxlength="450" v-model="form.cursos_observacao.value"
                                :disabled="!form.possui_cursos_complementares.value" fluid rows="3" cols="30" />
                            <label>Cursos Complementares *</label>
                        </FloatLabel>
                    </div>
                    <div class="flex pt-6 justify-between">
                        <Button label="Voltar" severity="secondary" icon="pi pi-arrow-left"
                            @click="activateCallback(1)" />
                        <Button label="Próximo" icon="pi pi-arrow-right" iconPos="right" @click="activateCallback(3)" />
                    </div>
                </StepPanel>
                <StepPanel v-slot="{ activateCallback }" :value="3">
                    <div class="flex flex-col gap-2 mx-auto" style="min-height: 16rem; max-width: 40rem">
                        <div class="text-center mt-4 mb-4 text-xl font-semibold">Dependentes</div>

                        <div class="flex flex-row flex-wrap gap-3 mb-6">
                            <div class="flex-1">
                                <ToggleButton class="w-full" v-model="form.possui_dependentes.value"
                                    onLabel="Possui Dependentes" offLabel="Não Possui Dependentes"
                                    @change="changePossuiDependentes" />
                            </div>
                            <div class="flex-1">
                                <FloatLabel>
                                    <InputNumber :disabled="!form.possui_dependentes.value"
                                        :invalid="form.numero_dependentes.validation_error"
                                        v-model="form.numero_dependentes.value" inputId="minmax"
                                        :min="form.numero_dependentes.min" :max="100" fluid />
                                    <label>N° Dependentes *</label>
                                </FloatLabel>
                                <small v-if="form.numero_dependentes.validation_error">Este campo é
                                    obrigatório.</small>
                            </div>
                        </div>
                        <div class="flex flex-col mb-6">
                            <FloatLabel>
                                <Textarea :invalid="form.observacao_dependentes.validation_error"
                                    v-model="form.observacao_dependentes.value"
                                    :disabled="!form.possui_dependentes.value" fluid rows="5" cols="30" />
                                <label>Observações (Idade, Necessidades) *</label>
                            </FloatLabel>
                            <small v-if="form.observacao_dependentes.validation_error">Este campo é obrigatório.</small>
                        </div>
                    </div>
                    <div class="flex pt-6 justify-between">
                        <Button label="Voltar" severity="secondary" icon="pi pi-arrow-left"
                            @click="activateCallback(2)" />
                        <Button label="Próximo" icon="pi pi-arrow-right" iconPos="right" @click="activateCallback(4)" />
                    </div>
                </StepPanel>
                <StepPanel v-slot="{ activateCallback }" :value="4">
                    <div class="flex flex-col gap-2 mx-auto" style="min-height: 16rem; max-width: 40rem">
                        <div class="text-center mt-4 mb-4 text-xl font-semibold">Endereço</div>
                        <div class="flex flex-row flex-wrap gap-3">
                            <div class="flex-1">
                                <div class="flex flex-col mb-6">
                                    <FloatLabel>
                                        <InputMask
                                            v-tooltip.bottom="'Se não tiver um CEP para inserir, você pode deixar este campo em branco.'"
                                            v-model="form.cep.value" mask="99999-999" placeholder="99999-999" fluid
                                            @update:modelValue="buscarCEP" />
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
                                        <Select v-model="form.uf.value" :options="ufs" fluid filter />
                                        <label>Estado</label>
                                    </FloatLabel>
                                </div>
                            </div>
                        </div>
                        <div class="flex flex-row flex-wrap gap-3">
                            <div class="flex-1">
                                <div class="flex flex-col mb-6">
                                    <FloatLabel>
                                        <InputText maxlength="150" :invalid="form.cidade.validation_error" fluid
                                            v-model="form.cidade.value" />
                                        <label>Cidade *</label>
                                    </FloatLabel>
                                    <small v-if="form.cidade.validation_error">Este campo é obrigatório.</small>
                                </div>
                            </div>
                            <div class="flex-1">
                                <div class="flex flex-col mb-6">
                                    <FloatLabel>
                                        <InputText maxlength="150" :invalid="form.bairro.validation_error" fluid
                                            v-model="form.bairro.value" />
                                        <label>Bairro *</label>
                                    </FloatLabel>
                                    <small v-if="form.bairro.validation_error">Este campo é obrigatório.</small>
                                </div>
                            </div>
                        </div>
                        <div class="flex flex-row flex-wrap gap-3">
                            <div class="flex-1">
                                <div class="flex flex-col mb-6">
                                    <FloatLabel>
                                        <InputText maxlength="250" :invalid="form.rua.validation_error" fluid
                                            v-model="form.rua.value" />
                                        <label>Rua *</label>
                                    </FloatLabel>
                                    <small v-if="form.rua.validation_error">Este campo é obrigatório.</small>
                                </div>
                            </div>
                            <div class="flex-1">
                                <FloatLabel>
                                    <InputNumber
                                        v-tooltip.bottom="'Se não tiver um número para inserir, você pode deixar este campo em branco.'"
                                        v-model="form.numero.value" inputId="minmax" :min="1" :max="999999" fluid />
                                    <label>Número</label>
                                </FloatLabel>
                            </div>
                        </div>
                        <FloatLabel class="mb-6">
                            <InputText maxlength="250" fluid
                                v-tooltip.bottom="'Se não tiver um complemento para inserir, você pode deixar este campo em branco.'"
                                v-model="form.complemento.value" />
                            <label>Complemento</label>
                        </FloatLabel>
                    </div>
                    <div class="flex pt-6 justify-between">
                        <Button label="Voltar" severity="secondary" icon="pi pi-arrow-left"
                            @click="activateCallback(3)" />
                        <Button label="Próximo" icon="pi pi-arrow-right" iconPos="right" @click="activateCallback(5)" />
                    </div>
                </StepPanel>
                <StepPanel v-slot="{ activateCallback }" :value="5">
                    <div class="flex flex-col gap-2 mx-auto" style="min-height: 16rem; max-width: 40rem">
                        <div class="text-center mt-4 mb-4 text-xl font-semibold">Experiência</div>
                        <ToggleButton class="w-full mb-6" v-model="form.possui_experiencia.value"
                            onLabel="Possui Experiência Profissional" offLabel="Não Possui Experiência Profissional"
                            @change="changePossuiExperiencia" />
                        <div class="flex justify-between gap-2">
                            <label>Experiência Profissional Anterior. *
                                <Tag severity="info"
                                    v-tooltip.bottom='`Avalie de 1 a 5 estrelas, onde 1 estrela representa "Não atende às expectativas" e 5 estrelas representa "Atende plenamente às expectativas".`'
                                    value="‎ ? ‎" rounded></Tag>
                            </label>
                            <div class="flex flex-col gap-2">
                                <div class="flex justify-end">
                                    <Rating :disabled="!form.possui_experiencia.value"
                                        v-model="form.relato_experiencia.value" />
                                </div>
                                <div class="flex justify-end">
                                    <small v-if="form.relato_experiencia.validation_error">Este campo é
                                        obrigatório.</small>
                                </div>
                            </div>
                        </div>
                        <div class="flex justify-between gap-2 mt-5 mb-8">
                            <label>Motivo da Saída dos Empregos Anteriores. *
                                <Tag severity="info"
                                    v-tooltip.bottom='`Avalie de 1 a 5 estrelas, onde 1 estrela representa "Não atende às expectativas" e 5 estrelas representa "Atende plenamente às expectativas".`'
                                    value="‎ ? ‎" rounded></Tag>
                            </label>
                            <div class="flex flex-col gap-2">
                                <div class="flex justify-end">
                                    <Rating :disabled="!form.possui_experiencia.value"
                                        v-model="form.relato_desligamento.value" />
                                </div>
                                <div class="flex justify-end">
                                    <small v-if="form.relato_desligamento.validation_error">Este campo é
                                        obrigatório.</small>
                                </div>
                            </div>
                        </div>
                        <div class="flex flex-col mb-6">
                            <FloatLabel>
                                <Textarea :invalid="form.observacao_experiencia.validation_error" maxlength="450"
                                    :disabled="!form.possui_experiencia.value"
                                    v-model="form.observacao_experiencia.value" fluid rows="5" cols="30" />
                                <label>Observações (Empresas, Cargos, etc.) *</label>
                            </FloatLabel>
                            <small v-if="form.observacao_experiencia.validation_error">Este campo é obrigatório.</small>
                        </div>
                    </div>
                    <div class="flex pt-6 justify-between">
                        <Button label="Voltar" severity="secondary" icon="pi pi-arrow-left"
                            @click="activateCallback(4)" />
                        <Button label="Próximo" icon="pi pi-arrow-right" iconPos="right" @click="activateCallback(6)" />
                    </div>
                </StepPanel>
                <StepPanel v-slot="{ activateCallback }" :value="6">
                    <div class="flex flex-col gap-2 mx-auto" style="min-height: 16rem; max-width: 40rem">
                        <div class="text-center mt-4 mb-4 text-xl font-semibold">Entrevista</div>
                        <div class="flex justify-between gap-2 mb-1">
                            <label>Por que você gostaria de trabalhar na nossa Empresa? *
                                <Tag severity="info"
                                    v-tooltip.bottom='`Avalie de 1 a 5 estrelas, onde 1 estrela representa "Não atende às expectativas" e 5 estrelas representa "Atende plenamente às expectativas".`'
                                    value="‎ ? ‎" rounded></Tag>
                            </label>
                            <div class="flex flex-col gap-2">
                                <div class="flex justify-end">
                                    <Rating v-model="form.relato_motivacao.value" />
                                </div>
                                <div class="flex justify-end">
                                    <small v-if="form.relato_motivacao.validation_error">Este campo é
                                        obrigatório.</small>
                                </div>
                            </div>
                        </div>
                        <label class="mb-6">Quais Lojas/Setores você tem interesse em atuar? Escolha até
                            2 opções. *</label>
                        <div class="flex flex-row flex-wrap gap-3 mb-2">
                            <div class="flex-1">
                                <div class="flex flex-col">
                                    <FloatLabel>
                                        <MultiSelect :invalid="form.lojas_interesse.validation_error"
                                            v-model="form.lojas_interesse.value" :options="lojas" optionLabel="name"
                                            filter :maxSelectedLabels="2" :selectionLimit="2" class="w-full" />
                                        <label for="ms-cities">Lojas *</label>
                                    </FloatLabel>
                                    <small v-if="form.lojas_interesse.validation_error">Este campo é
                                        obrigatório.</small>
                                </div>
                            </div>
                            <div class="flex-1">
                                <div class="flex flex-col">
                                    <FloatLabel>
                                        <MultiSelect :invalid="form.setores_interesse.validation_error"
                                            v-model="form.setores_interesse.value" :options="setores" optionLabel="name"
                                            filter :maxSelectedLabels="2" :selectionLimit="2" class="w-full" />
                                        <label for="ms-cities">Setores *</label>
                                    </FloatLabel>
                                    <small v-if="form.setores_interesse.validation_error">Este campo é
                                        obrigatório.</small>
                                </div>
                            </div>
                        </div>
                        <div class="flex justify-between gap-2 mb-6">
                            <label>Por que você escolheu essas lojas/setores? *
                                <Tag severity="info"
                                    v-tooltip.bottom='`Avalie de 1 a 5 estrelas, onde 1 estrela representa "Não atende às expectativas" e 5 estrelas representa "Atende plenamente às expectativas".`'
                                    value="‎ ? ‎" rounded></Tag>
                            </label>
                            <div class="flex flex-col gap-2">
                                <div class="flex justify-end">
                                    <Rating v-model="form.relato_interesse.value" />
                                </div>
                                <div class="flex justify-end">
                                    <small v-if="form.relato_interesse.validation_error">Este campo é
                                        obrigatório.</small>
                                </div>
                            </div>
                        </div>
                        <div class="flex justify-between gap-2 mb-2">
                            <label>Você prefere trabalhar em grupo ou sozinho? Por quê? *
                                <Tag severity="info"
                                    v-tooltip.bottom='`Avalie de 1 a 5 estrelas, onde 1 estrela representa "Não atende às expectativas" e 5 estrelas representa "Atende plenamente às expectativas".`'
                                    value="‎ ? ‎" rounded></Tag>
                            </label>
                            <div class="flex flex-col gap-2">
                                <div class="flex justify-end">
                                    <Rating v-model="form.relato_equipe.value" />
                                </div>
                                <div class="flex justify-end">
                                    <small v-if="form.relato_equipe.validation_error">Este campo é obrigatório.</small>
                                </div>
                            </div>
                        </div>
                        <ToggleButton class="w-full mb-6" v-model="form.restricoes_horario.value"
                            onLabel="Possui Restrição de Horário" offLabel="Não Possui Restrição de Horário" />
                        <div class="flex flex-col mb-4">
                            <FloatLabel>
                                <Textarea
                                    v-tooltip.bottom="'Se não tiver observações para inserir, você pode deixar este campo em branco.'"
                                    maxlength="450" v-model="form.observacoes_entrevista.value" fluid rows="3"
                                    cols="30" />
                                <label>Observações (Restrições horário, etc.)</label>
                            </FloatLabel>
                        </div>
                    </div>
                    <div class="flex pt-6 justify-between">
                        <Button label="Voltar" severity="secondary" icon="pi pi-arrow-left"
                            @click="activateCallback(5)" />
                        <Button label="Próximo" icon="pi pi-arrow-right" iconPos="right" @click="activateCallback(7)" />
                    </div>
                </StepPanel>
                <StepPanel v-slot="{ activateCallback }" :value="7">
                    <div class="flex flex-col gap-2 mx-auto" style="min-height: 16rem; max-width: 40rem">
                        <div class="text-center mt-4 mb-2 text-xl font-semibold">Considerações Finais</div>
                        <div class="flex flex-col mb-1">
                            <FloatLabel>
                                <InputText :invalid="form.entrevistador.validation_error" maxlength="200" fluid
                                    v-model="form.entrevistador.value" />
                                <label>Nome do Entrevistador *</label>
                            </FloatLabel>
                            <small v-if="form.entrevistador.validation_error">Este campo é obrigatório.</small>
                        </div>
                        <label class="mb-6">Quais Setores combinam com o perfil do candidato? *</label>
                        <div class="flex-1">
                            <div class="flex flex-col mb-2">
                                <FloatLabel>
                                    <MultiSelect :invalid="form.setores_ideal.validation_error"
                                        v-model="form.setores_ideal.value" :options="setores" optionLabel="name" filter
                                        class="w-full" />
                                    <label for="ms-cities">Setores *</label>
                                </FloatLabel>
                                <small v-if="form.setores_ideal.validation_error">Este campo é obrigatório.</small>
                            </div>
                        </div>
                        <ToggleButton class="w-full mb-2" v-model="form.apto_contratacao.value"
                            onLabel="Está Apto Para Contratação" offLabel="Não Está Apto Para Contratação" />
                        <ToggleButton class="w-full mb-2" v-model="form.ex_funcionario.value" onLabel="É Ex-Funcionário"
                            offLabel="Não É Ex-Funcionário" />
                        <ToggleButton class="w-full mb-2" v-model="form.atualmente_contratado.value"
                            onLabel="É Colaborador Atualmente" offLabel="Não é Colaborador Atualmente" />

                        <FloatLabel class="mb-4">
                            <Textarea
                                v-tooltip.bottom="'Se não tiver observações para inserir, você pode deixar este campo em branco.'"
                                maxlength="450" v-model="form.observacao.value" fluid rows="5" cols="30" />
                            <label>Observações Finais</label>
                        </FloatLabel>
                    </div>
                    <div class="flex pt-6 justify-between">
                        <Button label="Voltar" severity="secondary" icon="pi pi-arrow-left"
                            @click="activateCallback(6)" />
                        <Button v-if="editMode == false" label="Salvar" icon="pi pi-save" :loading="loadingSalvar"
                            iconPos="right" @click="salvar()" />
                        <Button v-if="editMode == true" label="Atualizar" icon="pi pi-save" :loading="loadingSalvar"
                            iconPos="right" @click="editar()" />
                    </div>
                </StepPanel>
            </StepPanels>
        </Stepper>
    </div>

    <Dialog v-model:visible="image.visible" modal header="Recortar Foto" :style="{ width: '50rem' }"
        :breakpoints="{ '1199px': '75vw', '575px': '90vw' }">
        <cropper class="cropper" ref="cropper" :src="image.src" :stencil-component="image.stencilComponent"
            :stencil-props="image.aspect" />
        <template #footer>
            <Button label="Cancelar" text severity="secondary" @click="image.visible = false" autofocus />
            <Button label="Salvar" outlined severity="secondary" @click="crop(image.mode)" autofocus />
        </template>
    </Dialog>

</template>

<script>
import { handleStoreErrors, handleDepartmentErrors, handleCurriculoErrors, handleSearchCurriculoErrors } from '@/common/utils';
import { api } from '@/service/api';
import { Cropper, CircleStencil } from 'vue-advanced-cropper';
import 'vue-advanced-cropper/dist/style.css';

function getMimeType(file, fallback = null) {
    const byteArray = (new Uint8Array(file)).subarray(0, 4);
    let header = '';
    for (let i = 0; i < byteArray.length; i++) {
        header += byteArray[i].toString(16);
    }
    switch (header) {
        case "89504e47":
            return "image/png";
        case "ffd8ffe0":
        case "ffd8ffe1":
        case "ffd8ffe2":
        case "ffd8ffe3":
        case "ffd8ffe8":
            return "image/jpeg";
        default:
            return fallback;
    }
}

export default {
    components: {
        Cropper,
        CircleStencil
    },
    data() {
        return {
            activeStep: 1,

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

            ufs_dict: [
                { sigla: "AC", nome: "Acre" },
                { sigla: "AL", nome: "Alagoas" },
                { sigla: "AP", nome: "Amapá" },
                { sigla: "AM", nome: "Amazonas" },
                { sigla: "BA", nome: "Bahia" },
                { sigla: "CE", nome: "Ceará" },
                { sigla: "DF", nome: "Distrito Federal" },
                { sigla: "ES", nome: "Espírito Santo" },
                { sigla: "GO", nome: "Goiás" },
                { sigla: "MA", nome: "Maranhão" },
                { sigla: "MT", nome: "Mato Grosso" },
                { sigla: "MS", nome: "Mato Grosso do Sul" },
                { sigla: "MG", nome: "Minas Gerais" },
                { sigla: "PA", nome: "Pará" },
                { sigla: "PB", nome: "Paraíba" },
                { sigla: "PR", nome: "Paraná" },
                { sigla: "PE", nome: "Pernambuco" },
                { sigla: "PI", nome: "Piauí" },
                { sigla: "RJ", nome: "Rio de Janeiro" },
                { sigla: "RN", nome: "Rio Grande do Norte" },
                { sigla: "RS", nome: "Rio Grande do Sul" },
                { sigla: "RO", nome: "Rondônia" },
                { sigla: "RR", nome: "Roraima" },
                { sigla: "SC", nome: "Santa Catarina" },
                { sigla: "SP", nome: "São Paulo" },
                { sigla: "SE", nome: "Sergipe" },
                { sigla: "TO", nome: "Tocantins" }
            ],

            setores: [],

            lojas: [],

            form: {
                apresentacao_curriculo: {
                    value: 0,
                    validation_error: false,
                    step: 1
                },
                apresentacao_pessoal: {
                    value: 0,
                    validation_error: false,
                    step: 1
                },
                apresentacao_observacao: {
                    value: '',
                    validation_error: false,
                    step: 1
                },
                foto: {
                    value: null,
                    step: 2
                },
                curriculo: {
                    value: null,
                    step: 2
                },
                nome: {
                    value: '',
                    validation_error: false,
                    step: 2
                },
                idade: {
                    value: null,
                    validation_error: false,
                    step: 2
                },
                cpf: {
                    value: '',
                    validation_error: false,
                    step: 2
                },
                rg: {
                    value: '',
                    step: 2
                },
                data_de_nascimento: {
                    value: '',
                    validation_error: false,
                    step: 2
                },
                telefone: {
                    value: '',
                    validation_error: false,
                    step: 2
                },
                telefone_adicional: {
                    value: '',
                    validation_error: false,
                    step: 2
                },
                estado_civil: {
                    value: '',
                    validation_error: false,
                    step: 2
                },
                escolaridade: {
                    value: '',
                    validation_error: false,
                    step: 2
                },
                possui_cursos_complementares: {
                    value: false,
                    validation_error: false,
                    step: 2
                },
                cursos_observacao: {
                    value: 'Não se aplica.',
                    validation_error: false,
                    step: 2
                },
                possui_dependentes: {
                    value: false,
                    step: 3
                },
                numero_dependentes: {
                    value: 0,
                    validation_error: false,
                    min: 0,
                    step: 3
                },
                observacao_dependentes: {
                    value: 'Não se aplica.',
                    validation_error: false,
                    step: 3
                },
                cep: {
                    value: '',
                    step: 4
                },
                uf: {
                    value: '',
                    step: 4
                },
                cidade: {
                    value: '',
                    validation_error: false,
                    step: 4
                },
                bairro: {
                    value: '',
                    validation_error: false,
                    step: 4
                },
                rua: {
                    value: '',
                    validation_error: false,
                    step: 4
                },
                numero: {
                    value: null,
                    step: 4
                },
                complemento: {
                    value: '',
                    step: 4
                },
                possui_experiencia: {
                    value: false,
                    step: 5
                },
                relato_experiencia: {
                    value: 0,
                    validation_error: false,
                    step: 5
                },
                relato_desligamento: {
                    value: 0,
                    validation_error: false,
                    step: 5
                },
                observacao_experiencia: {
                    value: 'Não se aplica.',
                    validation_error: false,
                    step: 5
                },
                relato_motivacao: {
                    value: 0,
                    validation_error: false,
                    step: 6
                },
                lojas_interesse: {
                    value: [],
                    validation_error: false,
                    step: 6
                },
                setores_interesse: {
                    value: [],
                    validation_error: false,
                    step: 6
                },
                relato_interesse: {
                    value: 0,
                    validation_error: false,
                    step: 6
                },
                relato_equipe: {
                    value: 0,
                    validation_error: false,
                    step: 6
                },
                restricoes_horario: {
                    value: false,
                    step: 6
                },
                observacoes_entrevista: {
                    value: '',
                    step: 6
                },
                entrevistador: {
                    value: '',
                    validation_error: false,
                    step: 7
                },
                setores_ideal: {
                    value: [],
                    validation_error: false,
                    step: 7
                },
                apto_contratacao: {
                    value: false,
                    step: 7
                },
                ex_funcionario: {
                    value: false,
                    step: 7
                },
                atualmente_contratado: {
                    value: false,
                    step: 7
                },
                observacao: {
                    value: '',
                    step: 7
                }

            },

            image: {
                src: null,
                type: null,
                mode: null,
                visible: false
            },

            cepTemp: '',
            loadingCep: false,

            loadingSalvar: false,
            loadingLojas: true,
            loadingSetores: true,
            loadingCurriculo: true,

            editMode: null,
        }
    },
    mounted() {
        this.form.cpf.value = String(this.$route.params.cpf);

        api.getCurriculo(this.form.cpf.value)
            .then(response => {
                console.log(response)
                this.form.apresentacao_curriculo.value = response.data.apresentacao_curriculo;
                this.form.apresentacao_pessoal.value = response.data.apresentacao_pessoal;
                this.form.apresentacao_observacao.value = response.data.apresentacao_observacao;
                if(response.data.foto){
                    console.log(response.data)
                    this.form.foto.value = {
                        id: response.data.foto.id,
                        foto: 'http://127.0.0.1:8000/' + response.data.foto.foto
                    };
                };
                if(response.data.curriculo){
                    this.form.curriculo.value = {
                        id: response.data.curriculo.id,
                        foto: 'http://127.0.0.1:8000/' + response.data.curriculo.foto
                    };
                };
                this.form.nome.value = response.data.nome;
                this.form.idade.value = response.data.idade;
                this.form.cpf.value = response.data.cpf;
                this.form.rg.value = response.data.rg;
                this.form.telefone.value = response.data.telefone;
                this.form.telefone_adicional.value = response.data.telefone_adicional;
                this.form.data_de_nascimento.value = this.dataStringToData(response.data.data_de_nascimento);
                this.form.estado_civil.value = response.data.estado_civil;
                this.form.escolaridade.value = response.data.escolaridade;
                this.form.possui_cursos_complementares.value = response.data.possui_cursos_complementares;
                this.form.cursos_observacao.value = response.data.cursos_observacao;
                this.form.possui_dependentes.value = response.data.possui_dependentes;
                this.form.numero_dependentes.value = response.data.numero_dependentes;
                this.form.observacao_dependentes.value = response.data.observacao_dependentes;
                this.form.cep.value = response.data.cep;
                this.form.uf.value = response.data.uf;
                this.form.cidade.value = response.data.cidade;
                this.form.bairro.value = response.data.bairro;
                this.form.rua.value = response.data.rua;
                this.form.numero.value = response.data.numero;
                this.form.complemento.value = response.data.complemento;
                this.form.possui_experiencia.value = response.data.possui_experiencia;
                this.form.relato_experiencia.value = response.data.relato_experiencia;
                this.form.relato_desligamento.value = response.data.relato_desligamento;
                this.form.observacao_experiencia.value = response.data.observacao_experiencia;
                this.form.relato_motivacao.value = response.data.relato_motivacao;
                this.form.lojas_interesse.value = response.data.lojas_interesse;
                this.form.setores_interesse.value = response.data.setores_interesse;
                this.form.relato_interesse.value = response.data.relato_interesse;
                this.form.relato_equipe.value = response.data.relato_equipe;
                this.form.restricoes_horario.value = response.data.restricoes_horario;
                this.form.observacoes_entrevista.value = response.data.observacoes_entrevista;
                this.form.entrevistador.value = response.data.entrevistador;
                this.form.setores_ideal.value = response.data.setores_ideal;
                this.form.apto_contratacao.value = response.data.apto_contratacao;
                this.form.ex_funcionario.value = response.data.ex_funcionario;
                this.form.atualmente_contratado.value = response.data.atualmente_contratado;
                this.form.observacao.value = response.data.observacao;
                this.editMode = true;
                this.loadingCurriculo = false;
            })
            .catch(error => {
                handleSearchCurriculoErrors(error, this.$router, this.$toast);
                this.editMode = false;
                this.loadingCurriculo = false;
            });

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
    },
    methods: {
        crop(mode) {
            const { canvas } = this.$refs.cropper.getResult();
            canvas.toBlob((blob) => {
                this.uploadFile(blob, mode);
            }, this.image.type);
        },
        loadImage(event, mode) {
            const { files } = event.target;
            if (files && files[0]) {
                if (this.image.src) {
                    URL.revokeObjectURL(this.image.src)
                }
                const blob = URL.createObjectURL(files[0]);

                const reader = new FileReader();

                reader.onload = (e) => {
                    if (mode == 'foto') {
                        this.image = {
                            src: blob,
                            type: getMimeType(e.target.result, files[0].type),
                            visible: true,
                            mode: mode,
                            stencilComponent: this.$options.components.CircleStencil,
                            aspect: { aspectRatio: 1 / 1 }
                        };
                    }
                    else if (mode == 'curriculo') {
                        this.image = {
                            src: blob,
                            type: getMimeType(e.target.result, files[0].type),
                            visible: true,
                            mode: mode,
                            stencilComponent: this.$options.components.RectangleStencil,
                            aspect: { aspectRatio: 210 / 297 }
                        };
                    }

                    event.target.value = null;
                };
                reader.readAsArrayBuffer(files[0]);
            }
        },
        uploadFile(blob, mode) {
            api.uploadFile(blob)
                .then(resp => {
                    let obj = {
                        id: resp.id,
                        foto: 'http://127.0.0.1:8000/' + resp.foto_url
                    }
                    if (mode == 'foto') {
                        this.form.foto.value = obj
                    }
                    else if (mode == 'curriculo') {
                        this.form.curriculo.value = obj
                    }
                    this.resetCrop();
                })
                .catch(error => console.log(error));
        },
        resetCrop() {
            this.image = {
                src: null,
                type: null,
                mode: null,
                visible: false
            }
        },
        changeCursosComplementares() {
            if (this.form.possui_cursos_complementares.value) {
                this.form.cursos_observacao.value = ''
            } else {
                this.form.cursos_observacao.value = 'Não se aplica.'
            }
        },
        changePossuiDependentes() {
            if (this.form.possui_dependentes.value) {
                this.form.numero_dependentes.value = 1
                this.form.numero_dependentes.min = 1
                this.form.observacao_dependentes.value = ''
            } else {
                this.form.numero_dependentes.value = 0
                this.form.numero_dependentes.min = 0
                this.form.observacao_dependentes.value = 'Não se aplica.'
            }
        },
        changePossuiExperiencia() {
            if (this.form.possui_experiencia.value) {
                this.form.relato_experiencia.value = 0
                this.form.relato_desligamento.value = 0
                this.form.observacao_experiencia.value = ''
            } else {
                this.form.relato_experiencia.value = 0
                this.form.relato_desligamento.value = 0
                this.form.observacao_experiencia.value = 'Não se aplica.'
            }
        },
        buscarCEP() {
            let cepNumerico = this.form.cep.value.replace(/\D/g, '');
            let alterouCep = this.cepTemp != cepNumerico;
            if (cepNumerico.length === 8 && alterouCep) {
                this.cepTemp = cepNumerico;
                this.loadingCep = true;

                fetch(`https://viacep.com.br/ws/${cepNumerico}/json/`)
                    .then(response => response.json())
                    .then(data => {
                        if (!data.erro) {

                            this.form.uf.value = this.ufs_dict.find(item => item.sigla === data.uf)?.nome;

                            this.form.cidade.value = data.localidade;
                            this.form.bairro.value = data.bairro;
                            this.form.rua.value = data.logradouro;

                            this.loadingCep = false;
                        } else {
                            this.loadingCep = false;
                            this.$toast.add({
                                severity: 'info',
                                summary: 'CEP não encontrado',
                                detail: 'Por favor informe os dados manualmente.',
                                life: 6000
                            });
                        }
                    })
                    .catch(error => {
                        this.loadingCep = false;
                        this.$toast.add({
                            severity: 'error',
                            summary: 'Erro ao buscar o CEP',
                            detail: 'Por favor informe os dados manualmente.',
                            life: 6000
                        });
                    });
            }
        },
        validarCampos() {
            let menorStep = 8;

            for (let key in this.form) {
                if (this.form.hasOwnProperty(key)) {
                    this.form[key].validation_error = false;
                }
            }

            if (this.form.apresentacao_curriculo.value == null ||
                this.form.apresentacao_curriculo.value == 0) {
                menorStep = Math.min(menorStep, this.form.apresentacao_curriculo.step);
                this.form.apresentacao_curriculo.validation_error = true;
            }

            if (this.form.apresentacao_pessoal.value == null ||
                this.form.apresentacao_pessoal.value == 0
            ) {
                menorStep = Math.min(menorStep, this.form.apresentacao_pessoal.step);
                this.form.apresentacao_pessoal.validation_error = true;
            }

            if (this.form.nome.value == null ||
                this.form.nome.value == ''
            ) {
                menorStep = Math.min(menorStep, this.form.nome.step);
                this.form.nome.validation_error = true;
            }

            if (this.form.idade.value == null ||
                this.form.idade.value < 1
            ) {
                menorStep = Math.min(menorStep, this.form.idade.step);
                this.form.idade.validation_error = true;
            }

            if (this.form.cpf.value == null ||
                this.form.cpf.value == ''
            ) {
                menorStep = Math.min(menorStep, this.form.cpf.step);
                this.form.cpf.validation_error = true;
            }

            if (this.form.telefone.value == null ||
                this.form.telefone.value == ''
            ) {
                menorStep = Math.min(menorStep, this.form.telefone.step);
                this.form.telefone.validation_error = true;
            }

            if (this.form.telefone_adicional.value == null ||
                this.form.telefone_adicional.value == ''
            ) {
                menorStep = Math.min(menorStep, this.form.telefone.step);
                this.form.telefone_adicional.validation_error = true;
            }

            if (this.form.data_de_nascimento.value == null ||
                this.form.data_de_nascimento.value == ''
            ) {
                menorStep = Math.min(menorStep, this.form.data_de_nascimento.step);
                this.form.data_de_nascimento.validation_error = true;
            }

            if (this.form.estado_civil.value == null ||
                this.form.estado_civil.value == ''
            ) {
                menorStep = Math.min(menorStep, this.form.estado_civil.step);
                this.form.estado_civil.validation_error = true;
            }

            if (this.form.escolaridade.value == null ||
                this.form.escolaridade.value == ''
            ) {
                menorStep = Math.min(menorStep, this.form.escolaridade.step);
                this.form.escolaridade.validation_error = true;
            }

            if (this.form.cursos_observacao.value == null ||
                this.form.cursos_observacao.value == ''
            ) {
                menorStep = Math.min(menorStep, this.form.cursos_observacao.step);
                this.form.cursos_observacao.validation_error = true;
            }

            if (this.form.numero_dependentes.value != 0 &&
                (this.form.numero_dependentes.value == null ||
                    this.form.numero_dependentes.value == '')
            ) {
                menorStep = Math.min(menorStep, this.form.numero_dependentes.step);
                this.form.numero_dependentes.validation_error = true;
            }

            if (this.form.observacao_dependentes.value == null ||
                this.form.observacao_dependentes.value == ''
            ) {
                menorStep = Math.min(menorStep, this.form.observacao_dependentes.step);
                this.form.observacao_dependentes.validation_error = true;
            }

            if (this.form.cidade.value == null ||
                this.form.cidade.value == ''
            ) {
                menorStep = Math.min(menorStep, this.form.cidade.step);
                this.form.cidade.validation_error = true;
            }

            if (this.form.bairro.value == null ||
                this.form.bairro.value == ''
            ) {
                menorStep = Math.min(menorStep, this.form.bairro.step);
                this.form.bairro.validation_error = true;
            }

            if (this.form.rua.value == null ||
                this.form.rua.value == ''
            ) {
                menorStep = Math.min(menorStep, this.form.rua.step);
                this.form.rua.validation_error = true;
            }

            if (this.form.relato_experiencia.value == null) {
                menorStep = Math.min(menorStep, this.form.relato_experiencia.step);
                this.form.relato_experiencia.validation_error = true;
            }

            if (this.form.relato_desligamento.value == null) {
                menorStep = Math.min(menorStep, this.form.relato_desligamento.step);
                this.form.relato_desligamento.validation_error = true;
            }

            if (this.form.observacao_experiencia.value == null ||
                this.form.observacao_experiencia.value == ''
            ) {
                menorStep = Math.min(menorStep, this.form.observacao_experiencia.step);
                this.form.observacao_experiencia.validation_error = true;
            }

            if (this.form.relato_motivacao.value == null ||
                this.form.relato_motivacao.value == 0
            ) {
                menorStep = Math.min(menorStep, this.form.relato_motivacao.step);
                this.form.relato_motivacao.validation_error = true;
            }

            if (this.form.lojas_interesse.value == null ||
                this.form.lojas_interesse.value == [] ||
                this.form.lojas_interesse.value == ''
            ) {
                menorStep = Math.min(menorStep, this.form.lojas_interesse.step);
                this.form.lojas_interesse.validation_error = true;
            }

            if (this.form.setores_interesse.value == null ||
                this.form.setores_interesse.value == [] ||
                this.form.setores_interesse.value == ''
            ) {
                menorStep = Math.min(menorStep, this.form.setores_interesse.step);
                this.form.setores_interesse.validation_error = true;
            }

            if (this.form.relato_interesse.value == null ||
                this.form.relato_interesse.value == 0
            ) {
                menorStep = Math.min(menorStep, this.form.relato_interesse.step);
                this.form.relato_interesse.validation_error = true;
            }

            if (this.form.relato_equipe.value == null ||
                this.form.relato_equipe.value == 0
            ) {
                menorStep = Math.min(menorStep, this.form.relato_equipe.step);
                this.form.relato_equipe.validation_error = true;
            }

            if (this.form.entrevistador.value == null ||
                this.form.entrevistador.value == ''
            ) {
                menorStep = Math.min(menorStep, this.form.entrevistador.step);
                this.form.entrevistador.validation_error = true;
            }

            if (this.form.setores_ideal.value == null ||
                this.form.setores_ideal.value == [] ||
                this.form.setores_ideal.value == ''
            ) {
                menorStep = Math.min(menorStep, this.form.setores_ideal.step);
                this.form.setores_ideal.validation_error = true;
            }

            if (menorStep < 8) {
                this.activeStep = menorStep;
                return false;
            } else {
                return true;
            }
        },
        dataToDataString(data) {
            const dia = String(data.getDate()).padStart(2, '0');
            const mes = String(data.getMonth() + 1).padStart(2, '0');
            const ano = data.getFullYear();

            return `${mes}-${dia}-${ano}`;
        },
        dataStringToData(dataString) {
            const [mes, dia, ano] = dataString.split('-').map(Number);
            return new Date(ano, mes - 1, dia);
        },
        salvar() {
            if (this.validarCampos()) {
                this.loadingSalvar = true;

                let data = {
                    apresentacao_curriculo: this.form.apresentacao_curriculo.value,
                    apresentacao_pessoal: this.form.apresentacao_pessoal.value,
                    apresentacao_observacao: this.form.apresentacao_observacao.value,
                    nome: this.form.nome.value,
                    idade: this.form.idade.value,
                    cpf: this.form.cpf.value,
                    rg: this.form.rg.value,
                    telefone: this.form.telefone.value,
                    telefone_adicional: this.form.telefone_adicional.value,
                    data_de_nascimento: this.dataToDataString(this.form.data_de_nascimento.value),
                    estado_civil: this.form.estado_civil.value,
                    escolaridade: this.form.escolaridade.value,
                    possui_cursos_complementares: this.form.possui_cursos_complementares.value,
                    cursos_observacao: this.form.cursos_observacao.value,
                    possui_dependentes: this.form.possui_dependentes.value,
                    numero_dependentes: this.form.numero_dependentes.value,
                    observacao_dependentes: this.form.observacao_dependentes.value,
                    cep: this.form.cep.value,
                    uf: this.form.uf.value,
                    cidade: this.form.cidade.value,
                    bairro: this.form.bairro.value,
                    rua: this.form.rua.value,
                    numero: this.form.numero.value,
                    complemento: this.form.complemento.value,
                    possui_experiencia: this.form.possui_experiencia.value,
                    relato_experiencia: this.form.relato_experiencia.value,
                    relato_desligamento: this.form.relato_desligamento.value,
                    observacao_experiencia: this.form.observacao_experiencia.value,
                    relato_motivacao: this.form.relato_motivacao.value,
                    lojas_interesse: this.form.lojas_interesse.value,
                    setores_interesse: this.form.setores_interesse.value,
                    relato_interesse: this.form.relato_interesse.value,
                    relato_equipe: this.form.relato_equipe.value,
                    restricoes_horario: this.form.restricoes_horario.value,
                    observacoes_entrevista: this.form.observacoes_entrevista.value,
                    entrevistador: this.form.entrevistador.value,
                    setores_ideal: this.form.setores_ideal.value,
                    apto_contratacao: this.form.apto_contratacao.value,
                    ex_funcionario: this.form.ex_funcionario.value,
                    atualmente_contratado: this.form.atualmente_contratado.value,
                    observacao: this.form.observacao.value
                };

                if(this.form.foto.value) data.foto = { id: this.form.foto.value.id };
                if(this.form.curriculo.value) data.curriculo = { id: this.form.curriculo.value.id };

                api.postAddCurriculo(data)
                    .then(response => {
                        this.$toast.add({
                            severity: 'success',
                            summary: 'Curriculo Adicionado com Sucesso',
                            life: 6000
                        });
                        this.$router.push('/');
                    })
                    .catch(error => {
                        handleCurriculoErrors(error, this.$router, this.$toast)
                        this.loadingSalvar = false;
                    });
            }
        },
        editar() {

            if (this.validarCampos()) {
                this.loadingSalvar = true;

                let data = {
                    apresentacao_curriculo: this.form.apresentacao_curriculo.value,
                    apresentacao_pessoal: this.form.apresentacao_pessoal.value,
                    apresentacao_observacao: this.form.apresentacao_observacao.value,
                    nome: this.form.nome.value,
                    idade: this.form.idade.value,
                    cpf: this.form.cpf.value,
                    rg: this.form.rg.value,
                    telefone: this.form.telefone.value,
                    telefone_adicional: this.form.telefone_adicional.value,
                    data_de_nascimento: this.dataToDataString(this.form.data_de_nascimento.value),
                    estado_civil: this.form.estado_civil.value,
                    escolaridade: this.form.escolaridade.value,
                    possui_cursos_complementares: this.form.possui_cursos_complementares.value,
                    cursos_observacao: this.form.cursos_observacao.value,
                    possui_dependentes: this.form.possui_dependentes.value,
                    numero_dependentes: this.form.numero_dependentes.value,
                    observacao_dependentes: this.form.observacao_dependentes.value,
                    cep: this.form.cep.value,
                    uf: this.form.uf.value,
                    cidade: this.form.cidade.value,
                    bairro: this.form.bairro.value,
                    rua: this.form.rua.value,
                    numero: this.form.numero.value,
                    complemento: this.form.complemento.value,
                    possui_experiencia: this.form.possui_experiencia.value,
                    relato_experiencia: this.form.relato_experiencia.value,
                    relato_desligamento: this.form.relato_desligamento.value,
                    observacao_experiencia: this.form.observacao_experiencia.value,
                    relato_motivacao: this.form.relato_motivacao.value,
                    lojas_interesse: this.form.lojas_interesse.value,
                    setores_interesse: this.form.setores_interesse.value,
                    relato_interesse: this.form.relato_interesse.value,
                    relato_equipe: this.form.relato_equipe.value,
                    restricoes_horario: this.form.restricoes_horario.value,
                    observacoes_entrevista: this.form.observacoes_entrevista.value,
                    entrevistador: this.form.entrevistador.value,
                    setores_ideal: this.form.setores_ideal.value,
                    apto_contratacao: this.form.apto_contratacao.value,
                    ex_funcionario: this.form.ex_funcionario.value,
                    atualmente_contratado: this.form.atualmente_contratado.value,
                    observacao: this.form.observacao.value
                };

                if(this.form.foto.value) data.foto = { id: this.form.foto.value.id };
                if(this.form.curriculo.value) data.curriculo = { id: this.form.curriculo.value.id };

                api.postEditCurriculo(data, this.form.cpf.value,)
                    .then(response => {
                        this.$toast.add({
                            severity: 'success',
                            summary: 'Curriculo Atualizado com Sucesso',
                            life: 6000
                        });
                        this.$router.push('/');
                    })
                    .catch(error => {
                        handleCurriculoErrors(error, this.$router, this.$toast)
                        this.loadingSalvar = false;
                    });
            }

        }
    },
    destroyed() {
        if (this.image.src) {
            URL.revokeObjectURL(this.image.src)
        }
    }
}
</script>
