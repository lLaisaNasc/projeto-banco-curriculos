<template>
    <FloatingConfigurator />
    <div class="bg-surface-50 dark:bg-surface-950 flex items-center justify-center min-h-screen min-w-[100vw] overflow-hidden">
        <div class="flex flex-col items-center justify-center">
            <div style="border-radius: 56px; padding: 0.3rem; background: linear-gradient(180deg, var(--primary-color) 10%)">
                <div class="w-full bg-surface-0 dark:bg-surface-900 py-20 px-8 sm:px-20" style="border-radius: 53px">
                    <div class="text-center mb-8">
                        <img src="/src/logo.png" alt="" width="200px" height="auto" class="mx-auto mb-4">
                        <span class="text-muted-color font-medium">Entre para continuar</span>
                    </div>
                    <div>
                        <label for="username1" class="block text-surface-900 dark:text-surface-0 text-xl font-medium mb-2">Usuário</label>
                        <InputText :invalid="invalid" id="username1" type="text" placeholder="Usuário" class="w-full md:w-[30rem] mb-8" v-model="username" />

                        <label for="password1" class="block text-surface-900 dark:text-surface-0 font-medium text-xl mb-2">Senha</label>
                        <Password :invalid="invalid" id="password1" v-model="password" placeholder="Senha" :toggleMask="true" class="mb-8" fluid :feedback="false" @keyup.enter="login" />

                        
                        <Button label="Entrar" class="w-full mt-2" :loading="loading" @click="login"></Button>
                    </div>
                </div>
            </div>
        </div>
    </div>
    <Toast />
    <ConfirmDialog />
</template>

<script>
import FloatingConfigurator from '@/components/FloatingConfigurator.vue';
import { api } from '@/service/api';
import { useRouter } from 'vue-router';

export default {
    components: {
        FloatingConfigurator,
    },
    data() {
        return {
            router: useRouter(),
            username: '',
            password: '',
            invalid: false,
            loading: false
        };
    },
    methods: {
        showToast(severity, summary, detail, life = 10000) {
            this.$toast.add({
                severity,
                summary,
                detail,
                life
            });
        },
        login() {
            this.loading = true;

            api.postLogin(this.username, this.password)
                .then(response => {
                    this.$router.push('/');
                })
                .catch(error => {
                    let severity = 'error';
                    let summary = 'Erro Desconhecido';
                    let detail = 'Ocorreu um erro inesperado. Por favor, entre em contato com o administrador do sistema para assistência.';

                    if (error.response?.status === 400) {
                        severity = 'warn';
                        summary = 'Preenchimento Incompleto';
                        detail = 'Por favor, preencha tanto o nome de usuário quanto a senha para continuar.';
                        this.invalid = true;
                    } else if (error.response?.status === 401) {
                        summary = 'Falha na Autenticação';
                        detail = 'O nome de usuário ou a senha fornecidos estão incorretos. Verifique suas credenciais e tente novamente.';
                        this.invalid = true;
                    } else if (error.code === "ERR_NETWORK") {
                        summary = 'Problema de Conexão';
                        detail = 'Não foi possível conectar ao servidor. Verifique sua conexão de rede e tente novamente mais tarde. Se o problema persistir, entre em contato com o administrador do sistema para obter assistência.';
                    }

                    this.showToast(severity, summary, detail);
                    this.loading = false;
                });
        }
    },
    created() {
        localStorage.removeItem('authToken');
        localStorage.removeItem('authRole');
        localStorage.removeItem('full_name');
        localStorage.removeItem('first_name');
        localStorage.removeItem('email');
        localStorage.removeItem('username');
    },
};
</script>
