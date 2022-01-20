$(function () {

    $.ajax({
        url: 'http://127.0.0.1:5000/listar_professor_disciplina',
        method: 'GET',
        dataType: 'json',
        success: listar,
        error: function () {
            alert("erro ao ler dados, verifique o backend");
        }
    });

    function listar(professor_disciplina) {
        for (var i in professor_disciplina) { //i vale a posição no vetor
            lin =
                '<tr>' + // elabora linha com os dados da pessoa
                '<td>' + professor_disciplina[i].professor.nome + '</td>' +
                '<td>' + professor_disciplina[i].professor.email + '</td>' +
                '<td>' + professor_disciplina[i].disciplina.nome + '</td>' +
                '<td>' + professor_disciplina[i].disciplina.ementa + '</td>' +
                '</tr>';
            // adiciona a linha no corpo da tabela
            $('#tabelaProfessorDisciplina').append(lin);
        }
    }
});