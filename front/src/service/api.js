import axios from 'axios';

const postman = axios.create({
    baseURL: 'http://127.0.0.1:8000/',
    timeout: 10000,
    headers: { 'Content-Type': 'application/json' }
});

const nonInterceptedEndpoints = ['/login/'];

postman.interceptors.request.use(config => {
    if (!nonInterceptedEndpoints.includes(config.url)) {
        const token = localStorage.getItem('authToken');

        if (token) {
            config.headers.Authorization = `Token ${token}`;
        }
    }
    return config;
}, error => {
    return Promise.reject(error);
});

postman.interceptors.response.use(response => {
    return response;
}, error => {
    if (error.response && error.response.status === 401) {
        const requestUrl = error.config.url;

        if (!nonInterceptedEndpoints.includes(requestUrl)) {
            window.location.href = '/auth/login';
        }
    }
    return Promise.reject(error);
});

export const api = {
    async postLogin(username, password) {
        const response = await postman.post('/login/', { username, password });

        localStorage.setItem('authToken', response.data.token);
        localStorage.setItem('authRole', response.data.role);
        localStorage.setItem('full_name', response.data.full_name);
        localStorage.setItem('first_name', response.data.first_name);
        localStorage.setItem('email', response.data.email);
        localStorage.setItem('username', response.data.username);
    },

    async getUsers() {
        return await postman.get('/users/');
    },
    async postAddUser(data) {
        const response = await postman.post('/users/add/', data);
    },

    async postEditUser(data, username) {
        const response = await postman.put(`/users/edit/${username}/`, data);
    },

    async deleteUser(username) {
        const response = await postman.delete(`/users/delete/${username}/`);
    },

    async postCloneUser(data) {
        const response = await postman.post(`/users/clone/`, data);
    },

    async getStores() {
        return await postman.get('/stores/');
    },

    async postAddStore(data) {
        const response = await postman.post('/stores/add/', data);
    },

    async postEditStore(data, id) {
        const response = await postman.put(`/stores/edit/${id}/`, data);
    },

    async deleteStore(id) {
        const response = await postman.delete(`/stores/delete/${id}/`);
    },

    async getDepartments() {
        return await postman.get('/departments/');
    },

    async postAddDepartment(data) {
        const response = await postman.post('/departments/add/', data);
    },

    async postEditDepartment(data, id) {
        const response = await postman.put(`/departments/edit/${id}/`, data);
    },

    async deleteDepartment(id) {
        const response = await postman.delete(`/departments/delete/${id}/`);
    },

    async getCurriculosCompleto() {
        return await postman.get('/curriculos/');
    },

    async getCurriculo(cpf) {
        return await postman.get(`/curriculos/${cpf}/`);
    },

    async postAddCurriculo(data) {
        const response = await postman.post('/curriculos/add/', data);
    },

    async postEditCurriculo(data, cpf) {
        const response = await postman.put(`/curriculos/edit/${cpf}/`, data);
    },

    async deleteCurriculo(cpf) {
        const response = await postman.delete(`/curriculos/delete/${cpf}/`);
    },

    async uploadFile(file) {
        let formData = new FormData();
        formData.append('foto', file);

        const response = await postman.post('/upload/foto/', formData, {
            headers: {
                'Content-Type': 'multipart/form-data'
            }
        });

        return response.data;
    },

    async deleteFile(id) {
        const response = await postman.delete(`upload/foto/delete/${id}/`);
    },

};
