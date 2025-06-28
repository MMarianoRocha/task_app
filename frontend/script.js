async function carregarTarefas() {
  try {
    const resposta = await fetch('http://127.0.0.1:5000/tarefas');
    const data = await resposta.json();

    const lista = document.getElementById('lista-tarefas');
    lista.innerHTML = '';

    data.tarefas.forEach(tarefa => {
      const item = document.createElement('li');
      item.innerHTML = `<strong>ID: ${tarefa.cod_id}</strong> <strong>${tarefa.titulo}</strong>: ${tarefa.descricao}`;
      lista.appendChild(item);
    });
  } catch (erro) {
    console.error('Erro ao carregar tarefas:', erro);
  }
}

async function adicionarTarefa() {
  const titulo = document.getElementById('titulo').value;
  const descricao = document.getElementById('descricao').value;

  if (!titulo || !descricao) {
    alert('Por favor, preencha todos os campos.');
    return;
  }

  try {
    const resposta = await fetch('http://127.0.1:5000/tarefas', {
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
    document.getElementById('titulo').value = '';
    document.getElementById('descricao').value = '';
    carregarTarefas();
  } catch (erro) {
    console.error('Erro ao adicionar tarefa:', erro);
    alert('Erro ao adicionar tarefa. Por favor, tente novamente.');
  }
}

  document.getElementById('adicionar_tarefa').addEventListener('click', function() {
  document.getElementById('container_input_tarefas').style.display = 'block';
});

