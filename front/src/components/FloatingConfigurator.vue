<template>
    <div class="fixed flex gap-4 top-8 right-8">
        <Button type="button" @click="toggleDarkMode" rounded :icon="{ 'pi pi-moon': isDarkTheme, 'pi pi-sun': !isDarkTheme }" severity="secondary" />
        <div class="relative">
            <Button
                icon="pi pi-palette"
                v-styleclass="{ selector: '@next', enterFromClass: 'hidden', enterActiveClass: 'animate-scalein', leaveToClass: 'hidden', leaveActiveClass: 'animate-fadeout', hideOnOutsideClick: true }"
                type="button"
                rounded
            />
            <AppConfigurator />
        </div>
    </div>
</template>

<script>
import AppConfigurator from '@/layout/AppConfigurator.vue';
import { useLayout } from '@/layout/composables/layout';

export default {
    name: 'FloatingConfigurator',
    components: {
        AppConfigurator
    },
    setup() {
        const { toggleDarkMode, isDarkTheme } = useLayout();

        return {
            toggleDarkMode,
            isDarkTheme,
        };
    },
    created() {
        document.documentElement.classList.toggle('app-dark', this.isDarkTheme);
    }
};
</script>
