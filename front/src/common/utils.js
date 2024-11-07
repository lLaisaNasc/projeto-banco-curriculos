export function handleUserErrors(error, router, toast) {
    let severity = 'error';
    let summary = 'Erro Desconhecido';
    let detail = 'Ocorreu um erro inesperado. Por favor, entre em contato com o administrador do sistema para assistência.';

    if (error.response?.status === 403) {
        router.push('/auth/access');
    }
    else if (error.response?.status === 400) {
        if (error.response?.data?.error === 'Missing required fields.') {
            summary = 'Erro';
            detail = 'Existem campos obrigatórios que não foram preenchidos.';
        } else if (error.response?.data?.error === 'Role not found.') {
            summary = 'Erro';
            detail = 'O grupo especificado não foi encontrado.';
        } else if (error.response?.data?.error === 'Invalid username.') {
            summary = 'Erro';
            detail = 'O nome de usuário informado é inválido.';
        } else if (error.response?.data?.error === 'Username already exists.') {
            summary = 'Erro';
            detail = 'O nome de usuário já está em uso. Tente outro.';
        }
        else if (error.response?.data?.error === "Cannot delete own user.") {
            summary = 'Erro';
            detail = 'Não é possível excluir o próprio usuário. Solicite a exclusão para outro administrador.';
        }
    } else if (error.response?.status === 404) {
        summary = 'Erro';
        detail = 'Usuário não encontrado.';
    }
    else if (error.code === "ERR_NETWORK") {
        summary = 'Problema de Conexão';
        detail = 'Não foi possível conectar ao servidor. Verifique sua conexão de rede e tente novamente mais tarde. Se o problema persistir, entre em contato com o administrador do sistema para obter assistência.';
    }

    toast.add({ severity: severity, summary: summary, detail: detail, life: 6000 });

};

export function handleStoreErrors(error, router, toast) {
    let severity = 'error';
    let summary = 'Erro Desconhecido';
    let detail = 'Ocorreu um erro inesperado. Por favor, entre em contato com o administrador do sistema para assistência.';

    if (error.response?.status === 403) {
        router.push('/auth/access');
    }
    else if (error.response?.status === 400) {
        if (error.response?.data?.error === 'Missing required fields.') {
            summary = 'Erro';
            detail = 'Existem campos obrigatórios que não foram preenchidos.';
        }
    } else if (error.response?.status === 404) {
        summary = 'Erro';
        detail = 'Loja não encontrada.';
    }
    else if (error.code === "ERR_NETWORK") {
        summary = 'Problema de Conexão';
        detail = 'Não foi possível conectar ao servidor. Verifique sua conexão de rede e tente novamente mais tarde. Se o problema persistir, entre em contato com o administrador do sistema para obter assistência.';
    }

    toast.add({ severity: severity, summary: summary, detail: detail, life: 6000 });
};

export function handleDepartmentErrors(error, router, toast) {
    let severity = 'error';
    let summary = 'Erro Desconhecido';
    let detail = 'Ocorreu um erro inesperado. Por favor, entre em contato com o administrador do sistema para assistência.';

    if (error.response?.status === 403) {
        router.push('/auth/access');
    }
    else if (error.response?.status === 400) {
        if (error.response?.data?.error === 'Missing required fields.') {
            summary = 'Erro';
            detail = 'Existem campos obrigatórios que não foram preenchidos.';
        }
    } else if (error.response?.status === 404) {
        summary = 'Erro';
        detail = 'Setor não encontrado.';
    }
    else if (error.code === "ERR_NETWORK") {
        summary = 'Problema de Conexão';
        detail = 'Não foi possível conectar ao servidor. Verifique sua conexão de rede e tente novamente mais tarde. Se o problema persistir, entre em contato com o administrador do sistema para obter assistência.';
    }

    toast.add({ severity: severity, summary: summary, detail: detail, life: 6000 });
};

export function handleCurriculoErrors(error, router, toast) {
    let severity = 'error';
    let summary = 'Erro Desconhecido';
    let detail = 'Ocorreu um erro inesperado. Por favor, entre em contato com o administrador do sistema para assistência.';

    if (error.response?.status === 403) {
        router.push('/auth/access');
    }
    else if (error.response?.status === 400) {
        if (error.response?.data?.error === 'Missing required fields.') {
            summary = 'Erro';
            detail = 'Existem campos obrigatórios que não foram preenchidos.';
        } else if (error.response?.data?.error === 'Curriculo already exists.') {
            summary = 'Erro';
            detail = 'Curriculo já cadastrado.';
        } else if (error.response?.data?.error === 'Store not found.') {
            summary = 'Erro';
            detail = 'Loja não encontrada.';
        } else if (error.response?.data?.error === 'Department not found.') {
            summary = 'Erro';
            detail = 'Setor não encontrado.';
        }
    } else if (error.response?.status === 404) {
        summary = 'Erro';
        detail = 'Curriculo não encontrado.';
    }
    else if (error.code === "ERR_NETWORK") {
        summary = 'Problema de Conexão';
        detail = 'Não foi possível conectar ao servidor. Verifique sua conexão de rede e tente novamente mais tarde. Se o problema persistir, entre em contato com o administrador do sistema para obter assistência.';
    }

    toast.add({ severity: severity, summary: summary, detail: detail, life: 6000 });
};

export function handleSearchCurriculoErrors(error, router, toast) {
    let severity = 'error';
    let summary = 'Erro Desconhecido';
    let detail = 'Ocorreu um erro inesperado. Por favor, entre em contato com o administrador do sistema para assistência.';

    if (error.response?.status === 403) {
        router.push('/auth/access');
    }
    else if (error.response?.status === 404) {
        return
    }
    else if (error.code === "ERR_NETWORK") {
        summary = 'Problema de Conexão';
        detail = 'Não foi possível conectar ao servidor. Verifique sua conexão de rede e tente novamente mais tarde. Se o problema persistir, entre em contato com o administrador do sistema para obter assistência.';
    }

    toast.add({ severity: severity, summary: summary, detail: detail, life: 6000 });
};