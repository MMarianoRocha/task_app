async function carregarTarefas() {
  try {
    const resposta = await fetch('http://127.0.0.1:5000/tarefas');
    const data = await resposta.json();

    const lista = document.getElementById('lista-tarefas');
    lista.innerHTML = '';

    data.tarefas.forEach(tarefa => {
      const item = document.createElement('li');
      item.innerHTML = `<strong>${tarefa.titulo}</strong>: ${tarefa.descricao}`;
      lista.appendChild(item);
    });
  } catch (erro) {
    console.error('Erro ao carregar tarefas:', erro);
  }
}
