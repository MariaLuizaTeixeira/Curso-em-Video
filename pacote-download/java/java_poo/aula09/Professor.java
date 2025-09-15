package aula09;
import java.util.Scanner;

public class Professor extends Pessoa{
    // Atributos
    private String especialidade;
    private float salario;

    // Getters e setters
    public String getEspecialidade() {
        return especialidade;
    }
    public void setEspecialidade(String especialidade) {
        this.especialidade = especialidade;
    }
    public float getSalario() {
        return salario;
    }
    public void setSalario(float salario) {
        this.salario = salario;
    }

    // Métodos
    public void receberAumento() {
        Scanner scanner = new Scanner(System.in);
        System.out.println("Insira o valor do aumento: ");
        setSalario(getSalario() + scanner.nextFloat());
        System.out.println("O novo salário é " + getSalario());
    }
    
}
