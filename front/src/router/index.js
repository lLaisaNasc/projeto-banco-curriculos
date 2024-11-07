import AppLayout from '@/layout/AppLayout.vue';
import { createRouter, createWebHistory } from 'vue-router';

const router = createRouter({
    history: createWebHistory(),
    routes: [
        {
            path: '/',
            component: AppLayout,
            children: [
                {
                    path: '/',
                    name: 'Consultar CPF',
                    component: () => import('@/views/pages/ConsultarCPF.vue'),
                    meta: { requiresAuth: true } 
                },
                {
                    path: '/cadastrar-curriculo/:cpf',
                    name: 'Cadastrar Currículo',
                    component: () => import('@/views/pages/cadastrar-curriculo/[cpf].vue'),
                    meta: { requiresAuth: true } 
                },
                {
                    path: '/rh/curriculos',
                    name: 'Banco de Currículos',
                    component: () => import('@/views/pages/BancoCurriculos.vue'),
                    meta: { requiresAuth: true, requiredRoles: ['rh', 'admin'] } 
                },
                {
                    path: '/admin/configuracoes',
                    name: 'Configurações',
                    component: () => import('@/views/pages/Configuracoes.vue'),
                    meta: { requiresAuth: true, requiredRoles: ['admin'] } 
                },
            ]
        },
        {
            path: '/pages/notfound',
            name: 'Não Encontrado',
            component: () => import('@/views/pages/NotFound.vue')
        },
        {
            path: '/auth/login',
            name: 'Login',
            component: () => import('@/views/pages/auth/Login.vue')
        },
        {
            path: '/auth/access',
            name: 'Acesso Negado',
            component: () => import('@/views/pages/auth/Access.vue')
        },
        {
            path: '/:pathMatch(.*)*',
            redirect: '/pages/notfound'
        }
    ]
});

router.beforeEach((to, from, next) => {
    const token = localStorage.getItem('authToken');
    const role = localStorage.getItem('authRole');
    const requiresAuth = to.matched.some(record => record.meta.requiresAuth);
    const requiredRoles = to.meta.requiredRoles || [];

    if (requiresAuth && (!token || !role)) {
        return next('/auth/login');
    }

    if (requiresAuth && requiredRoles.length > 0 && !requiredRoles.includes(role)) {
        return next('/auth/access');
    }

    next();
});

export default router;
