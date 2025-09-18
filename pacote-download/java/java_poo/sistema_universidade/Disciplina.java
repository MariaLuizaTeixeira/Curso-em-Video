package sistema_universidade;

public class Disciplina {
    // Atributos
    private String nome;
    private int carga_horaria;
    private Professor professor;
    private String alunos[];

    // Getters e setters
    public String getNome() {
        return nome;
    }
    public void setNome(String nome) {
        this.nome = nome;
    }
    public int getCarga_horaria() {
        return carga_horaria;
    }
    public void setCarga_horaria(int carga_horaria) {
        this.carga_horaria = carga_horaria;
    }
    public Professor getProfessor() {
        return professor;
    }
    public void setProfessor(Professor professor) {
        this.professor = professor;
    }
    public String[] getAlunos() {
        return alunos;
    }
    public void setAlunos(String[] alunos) {
        this.alunos = alunos;
    }
}
