<template>
    <ul class="layout-menu">
        <template v-for="(item, i) in filteredModel" :key="item.label">
            <app-menu-item v-if="!item.separator" :item="item" :index="i"></app-menu-item>
            <li v-if="item.separator" class="menu-separator"></li>
        </template>
    </ul>
</template>

<script>
import { ref, computed } from 'vue';
import AppMenuItem from './AppMenuItem.vue';

export default {
  name: 'AppMenu',
  components: {
    AppMenuItem
  },
  setup() {
    const role = localStorage.getItem('authRole'); 

    const model = ref([
      {
        label: 'Início',
        icon: 'pi pi-fw pi-briefcase',
        to: '/pages',
        items: [
          {
            label: 'Consultar CPF',
            icon: 'pi pi-fw pi-search',
            to: '/'
          },
          {
            label: 'Banco de Currículos',
            icon: 'pi pi-fw pi-users',
            to: '/rh/curriculos',
            roles: ['rh', 'admin'] 
          },
        ]
      },
      {
        label: 'Administrador',
        icon: 'pi pi-fw pi-briefcase',
        to: '/pages',
        items: [
          {
            label: 'Configurações',
            icon: 'pi pi-fw pi-cog',
            to: '/admin/configuracoes',
            roles: ['admin'] 
          }
        ]
      },
    ]);

    const filteredModel = computed(() => {
      return model.value.map(menuItem => {
        if (menuItem.items) {
          const filteredItems = menuItem.items.filter(subItem => {
            return !subItem.roles || subItem.roles.includes(role);
          });
          
          return filteredItems.length ? { ...menuItem, items: filteredItems } : null;
        }

        return !menuItem.roles || menuItem.roles.includes(role) ? menuItem : null;
      }).filter(Boolean); 
    });

    return {
      filteredModel
    };
  }
};
</script>
