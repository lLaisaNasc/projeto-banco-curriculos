import { createApp } from 'vue';
import App from './App.vue';
import router from './router';

import Aura from '@primevue/themes/aura';
import PrimeVue from 'primevue/config';
import ConfirmationService from 'primevue/confirmationservice';
import ToastService from 'primevue/toastservice';

import '@/assets/styles.scss';
import '@/assets/tailwind.css';

const app = createApp(App);

app.use(ToastService);
app.use(router);
app.use(PrimeVue, {
    theme: {
        preset: Aura,
        options: {
            darkModeSelector: '.app-dark'
        }
    },
    locale: {
        startsWith: 'Começa com',
        contains: 'Contém',
        notContains: 'Não contém',
        endsWith: 'Termina com',
        equals: 'Igual',
        notEquals: 'Diferente',
        noFilter: 'Sem filtro',
        lt: 'Menor que',
        lte: 'Menor ou igual a',
        gt: 'Maior que',
        gte: 'Maior ou igual a',
        dateIs: 'Data é',
        dateIsNot: 'Data não é',
        dateBefore: 'Data é antes',
        dateAfter: 'Data é depois',
        clear: 'Limpar',
        apply: 'Aplicar',
        matchAll: 'Corresponder a todos',
        matchAny: 'Corresponder a qualquer',
        addRule: 'Adicionar regra',
        removeRule: 'Remover regra',
        accept: 'Aceitar',
        reject: 'Rejeitar',
        choose: 'Escolher',
        upload: 'Carregar',
        cancel: 'Cancelar',
        completed: 'Concluído',
        pending: 'Pendente',
        fileSizeTypes: ['B', 'KB', 'MB', 'GB', 'TB', 'PB', 'EB', 'ZB', 'YB'],
        dayNames: ['Domingo', 'Segunda-feira', 'Terça-feira', 'Quarta-feira', 'Quinta-feira', 'Sexta-feira', 'Sábado'],
        dayNamesShort: ['Dom', 'Seg', 'Ter', 'Qua', 'Qui', 'Sex', 'Sáb'],
        dayNamesMin: ['D', 'S', 'T', 'Q', 'Q', 'S', 'S'],
        monthNames: ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro'],
        monthNamesShort: ['Jan', 'Fev', 'Mar', 'Abr', 'Mai', 'Jun', 'Jul', 'Ago', 'Set', 'Out', 'Nov', 'Dez'],
        chooseYear: 'Escolher Ano',
        chooseMonth: 'Escolher Mês',
        chooseDate: 'Escolher Data',
        prevDecade: 'Década Anterior',
        nextDecade: 'Próxima Década',
        prevYear: 'Ano Anterior',
        nextYear: 'Próximo Ano',
        prevMonth: 'Mês Anterior',
        nextMonth: 'Próximo Mês',
        prevHour: 'Hora Anterior',
        nextHour: 'Próxima Hora',
        prevMinute: 'Minuto Anterior',
        nextMinute: 'Próximo Minuto',
        prevSecond: 'Segundo Anterior',
        nextSecond: 'Próximo Segundo',
        am: 'am',
        pm: 'pm',
        today: 'Hoje',
        weekHeader: 'Sem',
        firstDayOfWeek: 0,
        showMonthAfterYear: false,
        dateFormat: 'dd/mm/yy',
        weak: 'Fraco',
        medium: 'Médio',
        strong: 'Forte',
        passwordPrompt: 'Digite uma senha',
        searchMessage: '{0} resultados disponíveis',
        selectionMessage: '{0} itens selecionados',
        emptySelectionMessage: 'Nenhum item selecionado',
        emptySearchMessage: 'Nenhum resultado encontrado',
        fileChosenMessage: '{0} arquivos',
        noFileChosenMessage: 'Nenhum arquivo escolhido',
        emptyMessage: 'Nenhuma opção disponível',
        aria: {
            trueLabel: 'Verdadeiro',
            falseLabel: 'Falso',
            nullLabel: 'Não Selecionado',
            star: '1 estrela',
            stars: '{star} estrelas',
            selectAll: 'Todos os itens selecionados',
            unselectAll: 'Todos os itens desmarcados',
            close: 'Fechar',
            previous: 'Anterior',
            next: 'Próximo',
            navigation: 'Navegação',
            scrollTop: 'Rolar para o Topo',
            moveTop: 'Mover para o Topo',
            moveUp: 'Mover para Cima',
            moveDown: 'Mover para Baixo',
            moveBottom: 'Mover para o Fundo',
            moveToTarget: 'Mover para o Destino',
            moveToSource: 'Mover para a Origem',
            moveAllToTarget: 'Mover Tudo para o Destino',
            moveAllToSource: 'Mover Tudo para a Origem',
            pageLabel: 'Página {page}',
            firstPageLabel: 'Primeira Página',
            lastPageLabel: 'Última Página',
            nextPageLabel: 'Próxima Página',
            prevPageLabel: 'Página Anterior',
            rowsPerPageLabel: 'Linhas por página',
            jumpToPageDropdownLabel: 'Pular para a Página Dropdown',
            jumpToPageInputLabel: 'Pular para a Página Input',
            selectRow: 'Linha Selecionada',
            unselectRow: 'Linha Desmarcada',
            expandRow: 'Linha Expandida',
            collapseRow: 'Linha Recolhida',
            showFilterMenu: 'Mostrar Menu de Filtro',
            hideFilterMenu: 'Esconder Menu de Filtro',
            filterOperator: 'Operador de Filtro',
            filterConstraint: 'Restrição de Filtro',
            editRow: 'Editar Linha',
            saveEdit: 'Salvar Edição',
            cancelEdit: 'Cancelar Edição',
            listView: 'Visualização em Lista',
            gridView: 'Visualização em Grade',
            slide: 'Slide',
            slideNumber: '{slideNumber}',
            zoomImage: 'Ampliar Imagem',
            zoomIn: 'Aproximar',
            zoomOut: 'Afastar',
            rotateRight: 'Girar para a Direita',
            rotateLeft: 'Girar para a Esquerda'
        }
    }
});
app.use(ConfirmationService);

app.mount('#app');
