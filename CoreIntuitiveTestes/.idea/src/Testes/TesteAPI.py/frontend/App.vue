<template>
    <div id="app">
    <h1>Buscar Operadoras de Saúde</h1>
    <input v-model="query" @input="search" placeholder="Digite o nome da operadora" />

    <div v-if="results.length > 0">
        <ul>
        <li v-for="(operator, index) in results" :key="index">
            {{ operator.operator_name }} - {{ operator.cnpj }}
        </li>
        </ul>
    </div>

    <div v-else>
        <p>Nenhum resultado encontrado.</p>
    </div>
    </div>
</template>

<script>
import { searchOperators } from './api';

export default {
    data() {
    return {
        query: '',
        results: []
    };
    },
    methods: {
    async search() {
        if (this.query.length >= 3) {
        try {
            const response = await searchOperators(this.query);
            this.results = response.data;
        } catch (error) {
            console.error('Erro ao buscar:', error);
        }
        } else {
        this.results = [];
        }
    }
    }
};
</script>

<style scoped>
#app {
    text-align: center;
    margin-top: 50px;
}

input {
    padding: 8px;
    width: 300px;
    margin-bottom: 20px;
}

ul {
    list-style-type: none;
    padding: 0;
}

li {
    background: #f4f4f4;
    padding: 10px;
    margin: 5px 0;
}
</style>
