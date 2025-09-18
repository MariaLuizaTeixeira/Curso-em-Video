package aula08;
public class Professor extends Pessoa{
    // Atributos
    private String especialidade;
    private float salario;

    // Getters e setters
    public String getEspecialidade() {
        return especialidade;
    }

    public float getSalario() {
        return salario;
    }

    public void setEspecialidade(String especialidade) {
        this.especialidade = especialidade;
    }

    public void setSalario(float salario) {
        this.salario = salario;
    }
    
    // Métodos
    public void receberAumento(float aum) {
        setSalario(getSalario() + aum);
    }
}
