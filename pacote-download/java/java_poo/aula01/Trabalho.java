package aula01;
public class Trabalho {
    String funcao;
    String data_entrada;
    int horas_semanais;
    float salario;
    boolean no_trabalho;

    void chegar() {
        if (no_trabalho == true) {
            System.out.println("Você já está no trabalho.");
        }

        else {
            System.out.println("Você chegou no trabalho.");
            no_trabalho = true;
        }
    }

    void sair() {
        if (no_trabalho == false) {
            System.out.println("Você já está fora do trabalho.");
        }

        else {
            System.out.println("Você saiu do trabalho.");
            no_trabalho = false;
        }
    }

    void trabalhar() {
        System.out.println("Você está trabalhando.");
    }
}
