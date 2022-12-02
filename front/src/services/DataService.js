import { BASE_API_URL } from "./Common";

const axios = require('axios');

const DataService = {
    Init: function () {
        // Any application initialization logic comes here
    },
    GetSumAll: async function () {
        return await axios.get(BASE_API_URL );
    },
    GetNat: async function () {
        return await axios.get(BASE_API_URL+ 'national' );
    },
    GetInterNAt: async function () {
        return await axios.get(BASE_API_URL+'inter' );
    },
    GetTech: async function () {
        return await axios.get(BASE_API_URL+'tech' );
    },
    GetSport: async function () {
        return await axios.get(BASE_API_URL+'sport' );
    },


}

export default DataService;