<template>
    <div class="layout-topbar">
        <div class="layout-topbar-logo-container">
            <button class="layout-menu-button layout-topbar-action" @click="onMenuToggle">
                <i class="pi pi-bars"></i>
            </button>
            <router-link to="/" class="layout-topbar-logo">

                <img src="/src/logo.png" alt="Logo" style="width:40px; height: auto;" />
            </router-link>
        </div>

        <div class="layout-topbar-actions">
            <div class="layout-config-menu">
                <button type="button" class="layout-topbar-action" @click="toggleDarkMode">
                    <i :class="['pi', { 'pi-moon': isDarkTheme, 'pi-sun': !isDarkTheme }]"></i>
                </button>
                <div class="relative">
                    <button
                        v-styleclass="{ selector: '@next', enterFromClass: 'hidden', enterActiveClass: 'animate-scalein', leaveToClass: 'hidden', leaveActiveClass: 'animate-fadeout', hideOnOutsideClick: true }" 
                        type="button" 
                        class="layout-topbar-action "
                    >
                        <i class="pi pi-user"></i>
                    </button>
                    <AppConfigurator />
                </div>
            </div>
        </div>
    </div>
</template>

<script>
import { useLayout } from '@/layout/composables/layout';
import AppConfigurator from './AppConfigurator.vue';

export default {
    data() {
        const { onMenuToggle, toggleDarkMode, isDarkTheme } = useLayout();

        return {
            onMenuToggle,
            toggleDarkMode,
            isDarkTheme
        };
    },
    components: {
        AppConfigurator,
    },
    created() {
        document.documentElement.classList.toggle('app-dark', this.isDarkTheme);
    },
};
</script>


