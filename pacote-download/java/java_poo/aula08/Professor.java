package aula08;
public class Professor extends Pessoa{
    // Atributos
    private String especialidade;
    private float salario;

    // Construtor
    public Professor(String nome, int idade, String sexo, String especialidade, float salario) {
        super(nome, idade, sexo);
        this.especialidade = especialidade;
        this.salario = salario;
    }

    // Getters e setters
    public String getEspecialidade() {
        return especialidade;
    }

    public float getSalario() {
        return salario;
    }

    // Métodos
    public void receberAumento() {
        
    }
}
