import { computed, reactive, readonly } from 'vue';

const layoutConfig = reactive({
    preset: localStorage.getItem('layoutPreset') || 'Aura',
    primary: localStorage.getItem('layoutPrimary') || 'rose',
    surface: localStorage.getItem('layoutSurface') || 'viva',
    darkTheme: JSON.parse(localStorage.getItem('layoutDarkTheme')) || false,
    menuMode: localStorage.getItem('layoutMenuMode') || 'static'
});

const layoutState = reactive({
    staticMenuDesktopInactive: false,
    overlayMenuActive: false,
    profileSidebarVisible: false,
    configSidebarVisible: false,
    staticMenuMobileActive: false,
    menuHoverActive: false,
    activeMenuItem: null
});

export function useLayout() {
    const setPrimary = (value) => {
        layoutConfig.primary = value;
        localStorage.setItem('layoutPrimary', value);
    };

    const setSurface = (value) => {
        layoutConfig.surface = value;
        localStorage.setItem('layoutSurface', value);
    };

    const setPreset = (value) => {
        layoutConfig.preset = value;
        localStorage.setItem('layoutPreset', value);
    };
    
    const setActiveMenuItem = (item) => {
        layoutState.activeMenuItem = item.value || item;
    };

    const setMenuMode = (mode) => {
        layoutConfig.menuMode = mode;
        localStorage.setItem('layoutMenuMode', mode);
    };

    const toggleDarkMode = () => {
        if (!document.startViewTransition) {
            executeDarkModeToggle();

            return;
        }

        document.startViewTransition(() => executeDarkModeToggle(event));
    };

    const executeDarkModeToggle = () => {
        layoutConfig.darkTheme = !layoutConfig.darkTheme;
        document.documentElement.classList.toggle('app-dark');
        localStorage.setItem('layoutDarkTheme', layoutConfig.darkTheme);
    };

    const onMenuToggle = () => {
        if (layoutConfig.menuMode === 'overlay') {
            layoutState.overlayMenuActive = !layoutState.overlayMenuActive;
        }

        if (window.innerWidth > 991) {
            layoutState.staticMenuDesktopInactive = !layoutState.staticMenuDesktopInactive;
        } else {
            layoutState.staticMenuMobileActive = !layoutState.staticMenuMobileActive;
        }
    };

    const resetMenu = () => {
        layoutState.overlayMenuActive = false;
        layoutState.staticMenuMobileActive = false;
        layoutState.menuHoverActive = false;
    };

    const isSidebarActive = computed(() => layoutState.overlayMenuActive || layoutState.staticMenuMobileActive);
    
    const isDarkTheme = computed(() => layoutConfig.darkTheme);
    
    const getPrimary = computed(() => layoutConfig.primary);

    const getSurface = computed(() => layoutConfig.surface);

    return { 
        layoutConfig: readonly(layoutConfig), 
        layoutState: readonly(layoutState), 
        onMenuToggle, 
        isSidebarActive, 
        isDarkTheme, 
        getPrimary, 
        getSurface, 
        setActiveMenuItem, 
        toggleDarkMode, 
        setPrimary, 
        setSurface, 
        setPreset, 
        resetMenu, 
        setMenuMode 
    };
}
