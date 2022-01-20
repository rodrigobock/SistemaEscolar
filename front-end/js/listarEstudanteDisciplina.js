$(function () {

    $.ajax({
        url: 'http://127.0.0.1:5000/listar_aluno_disciplina',
        method: 'GET',
        dataType: 'json',
        success: listar,
        error: function () {
            alert("erro ao ler dados, verifique o backend");
        }
    });

    function listar(aluno_disciplina) {
        for (var i in aluno_disciplina) { //i vale a posição no vetor
            lin = '<tr>' + // elabora linha com os dados da pessoa
                '<td>' + aluno_disciplina[i].aluno.nome + '</td>' +
                '<td>' + aluno_disciplina[i].aluno.email + '</td>' +
                '<td>' + aluno_disciplina[i].disciplina.nome + '</td>' +
                '<td>' + aluno_disciplina[i].disciplina.ementa + '</td>' +
                '<td>' + aluno_disciplina[i].semestre + '</td>' +
                '<td>' + aluno_disciplina[i].mediaFinal + '</td>' +
                '<td>' + aluno_disciplina[i].frequencia + '</td>' +
                '</tr>';
            // adiciona a linha no corpo da tabela
            $('#tabelaAlunoDisciplina').append(lin);
        }
    }
});