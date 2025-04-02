<template>
  <div id="app">
    <h1>Busca de Operadoras</h1>
    <input v-model="searchTerm" @input="buscarOperadora" placeholder="Digite o nome da operadora">
    
    <div v-if="operadoras.length > 0">
      <h2>Resultados:</h2>
      <ul>
        <li v-for="operadora in operadoras" :key="operadora.CNPJ">
          <p><strong>CNPJ:</strong> {{ operadora.CNPJ }}</p>
          <p><strong>Razão Social:</strong> {{ operadora.Razao_Social }}</p>
          <p><strong>Nome Fantasia:</strong> {{ operadora.Nome_Fantasia }}</p>
          <p><strong>Modalidade:</strong> {{ operadora.Modalidade }}</p>
        </li>
      </ul>
    </div>
    <div v-else>
      <p>Nenhum resultado encontrado.</p>
    </div>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  name: 'App',
  data() {
    return {
      searchTerm: '', // O termo de busca
      operadoras: [], // Resultados da busca
    };
  },
  methods: {
    async buscarOperadora() {
      if (this.searchTerm === '') {
        this.operadoras = []; // Limpar resultados se a busca estiver vazia
        return;
      }

      try {
        // Enviando a busca para o servidor Flask
        const response = await axios.get(`http://localhost:5000/buscar?q=${this.searchTerm}`);
        
        // Atualizando a lista de operadoras com os dados retornados
        this.operadoras = response.data;
      } catch (error) {
        console.error("Erro ao buscar operadora:", error);
        this.operadoras = []; // Limpar resultados em caso de erro
      }
    },
  },
};
</script>

<style scoped>
/* Estilos básicos */
#app {
  text-align: center;
  margin-top: 50px;
}
input {
  padding: 10px;
  width: 250px;
  font-size: 16px;
}
ul {
  list-style-type: none;
  padding: 0;
}
li {
  padding: 10px;
  background-color: #f1f1f1;
  margin-bottom: 10px;
  border-radius: 5px;
}
h2 {
  color: #19c463;
}
</style>
