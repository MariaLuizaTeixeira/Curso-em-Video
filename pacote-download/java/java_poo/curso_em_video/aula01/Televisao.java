package aula01;
import java.util.Scanner;
public class Televisao {
    String cor;
    String marca;
    int ano_producao;
    int ano_validade;
    float polegadas;
    float canal;
    int resolucao;
    boolean ligada;

    void ligar() {
        if (ligada == true) {
            System.out.println("A TV já está ligada.");
        }

        else {
            System.out.println("TV ligada.");
            ligada = true;
        }
    }

    void desligar() {
        if (ligada == false) {
            System.out.println("A TV já está desligada.");
        }

        else {
            System.out.println("TV desligada.");
            ligada = false;
        }
    }

    void mudar_canal() {
        Scanner scanner = new Scanner(System.in);
        System.out.println("Digite o número do canal desejado: ");
        this.canal = scanner.nextFloat();
        System.out.println("Canal mudado para canal " + this.canal);
        scanner.close();
    }

}
