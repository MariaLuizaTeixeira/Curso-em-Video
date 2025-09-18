package aula08;
public class Aluno extends Pessoa {
    // Atributos
    private int matricula;
    private String curso;
    
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
        System.out.println("Matrícula será cancelada.");
    }

    public void PagarMensalidade() {
        System.out.println("Matrícula será cancelada.");
    }
}
