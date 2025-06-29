async function carregarTarefas() {
  try {
    const resposta = await fetch('http://127.0.0.1:5000/tarefas');
    const data = await resposta.json();

    const lista = document.getElementById('lista-tarefas');
    lista.innerHTML = '';

    data.tarefas.forEach(tarefa => {
      const item = document.createElement('li');
      const statusTexto = tarefa.status === 'concluido' ? 'Concluído' : 'Em andamento';
      item.innerHTML = `<strong>ID: ${tarefa.cod_id}</strong> <strong>${tarefa.titulo}</strong>: ${tarefa.descricao} <br> <em>Data de criação: ${tarefa.data_criacao}</em> <br> <span>Status: ${statusTexto}</span>`;
      lista.appendChild(item);
    });
  } catch (erro) {
    console.error('Erro ao carregar tarefas:', erro);
  }
}


async function adicionarTarefa() {
  const titulo = document.getElementById('titulo_tarefa').value;
  const descricao = document.getElementById('descricao').value;
  if (!titulo || !descricao) {
    alert('Por favor, preencha todos os campos.');
    return;
  }
  try {
    const resposta = await fetch('http://127.0.0.1:5000/tarefas', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify({ titulo, descricao })
    });
    if (!resposta.ok) {
      throw new Error('Erro ao adicionar tarefa');
    }
    const data = await resposta.json();
    console.log('Tarefa adicionada:', data);
    document.getElementById('titulo_tarefa').value = '';
    document.getElementById('descricao').value = '';
    carregarTarefas();
  } catch (erro) {
    console.error('Erro ao adicionar tarefa:', erro);
    alert('Erro ao adicionar tarefa. Por favor, tente novamente.');
  }
}

async function removerTarefa() {
  const id = document.getElementById('id_tarefa').value;
  if (!id) {
    alert('Por favor, informe o ID da tarefa.');
    return;
  }
  try {
    const resposta = await fetch('http://127.0.0.1:5000/tarefas', {
      method: 'DELETE',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify({ cod_id: id })
    });
    if (!resposta.ok) {
      throw new Error('Erro ao remover tarefa');
    }
    carregarTarefas();
    document.getElementById('id_tarefa').value = '';
  } catch (erro) {
    console.error('Erro ao remover tarefa:', erro);
    alert('Erro ao remover tarefa. Por favor, tente novamente.');
  }
}


// Exibir/ocultar containers
document.getElementById('adicionar_tarefa').addEventListener('click', function() {
  document.getElementById('container_input_tarefas').style.display = 'block';
  document.getElementById('container_remove_tarefas').style.display = 'none';
});
document.getElementById('remover_tarefa').addEventListener('click', function() {
  document.getElementById('container_input_tarefas').style.display = 'none';
  document.getElementById('container_remove_tarefas').style.display = 'block';
});
// Ocultar ambos ao iniciar
window.onload = function() {
  document.getElementById('container_input_tarefas').style.display = 'none';
  document.getElementById('container_remove_tarefas').style.display = 'none';
  carregarTarefas();
};


