package aula08;
public class Aluno extends Pessoa {
    // Atributos
    private int matricula;
    private String curso;

    // Construtor
    public Aluno(String nome, int idade, String sexo, int matricula, String curso) {
        super(nome, idade, sexo);
        this.matricula = matricula;
        this.curso = curso;
    }

    // Getters e setters
    public int getMatricula() {
        return matricula;
    }
    public void setMatricula(int matricula) {
        this.matricula = matricula;
    }
    public String getCurso() {
        return curso;
    }
    public void setCurso(String curso) {
        this.curso = curso;
    }
    
    // Métodos
    public void cancelarMatricula() {
        
    }
}
