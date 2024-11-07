<template>
    <div class="card">
        <Tabs value="0">
            <TabList>
                <Tab value="0">Usuários</Tab>
                <Tab value="1">Lojas</Tab>
                <Tab value="2">Setores</Tab>
            </TabList>
            <TabPanels>
                <TabPanel value="0">
                    <CadastroUsuarios />
                </TabPanel>
                <TabPanel value="1">
                    <CadastroLojas />
                </TabPanel>
                <TabPanel value="2">
                    <CadastroSetores />
                </TabPanel>
            </TabPanels>
        </Tabs>
    </div>
</template>

<script>
import CadastroUsuarios from '@/components/CadastroUsuarios.vue';
import CadastroLojas from '@/components/CadastroLojas.vue';
import CadastroSetores from '@/components/CadastroSetores.vue';

export default {
    components: {
        CadastroUsuarios,
        CadastroLojas,
        CadastroSetores
    },
};
</script>

<style>
.p-tabpanels {
 padding-left: 0 !important; 
 padding-right: 0 !important;
}
</style>

