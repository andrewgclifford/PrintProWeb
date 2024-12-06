import axios from 'axios';

const instance = axios.create({
    baseURL: 'http://VM_IP:8000/api'
});

export default instance; 