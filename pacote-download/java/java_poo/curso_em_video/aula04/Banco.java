package aula04;
import java.util.Scanner;

public class Banco {
    Scanner scanner = new Scanner(System.in);

    private int numConta;
    private String tipo;
    private String dono;
    private float saldo;
    private boolean status;
    private float transicao;

    public int getNumConta() {
        return numConta;
    }
    public void setNumConta(int numConta) {
        this.numConta = numConta;
    }
    public String getTipo() {
        return tipo;
    }
    public void setTipo(String tipo) {
        this.tipo = tipo;
    }
    public String getDono() {
        return dono;
    }
    public void setDono(String dono) {
        this.dono = dono;
    }
    public float getSaldo() {
        return saldo;
    }
    public void setSaldo(float saldo) {
        this.saldo = saldo;
    }
    public boolean getStatus() {
        return status;
    }
    public void setStatus(boolean status) {
        this.status = status;
    }
    public Banco(int numConta) {
        this.numConta = numConta;
        this.saldo = 0;
    }

    public void abrirConta() {
        do {
            System.out.println("Insira o tipo da conta:\n [CC] - Conta corrente\n [CP] - conta poupança");
            setTipo(scanner.nextLine());
            if (getTipo() == "CC" || getTipo() == "CP") {
                System.out.println("Tipo não aceito.");
            }
        } while (getTipo() == "CC" || getTipo() == "CP");

        if (getTipo() == "CC") {
            setSaldo(saldo + 50);
        }

        else {
            setSaldo(saldo + 150);
        }

        setStatus(true);
    }

    public void fecharConta() {
        if (getSaldo() != 0 || getStatus() == false) {
            System.out.println("Para fechar a conta, o saldo deve ser R$ 0,00 e conta deve estar aberta.");
        }

        else {
            System.out.println("Sua conta foi fechada.");
            setStatus(false);
        }
    }

    public void depositar() {
        if (getStatus() == false) {
            System.out.println("Para depositar, a conta precisa estar aberta.");
        }

        else {
            System.out.println("Insira o valor a ser depositado:");
            this.transicao = scanner.nextFloat();
            setSaldo(saldo + transicao);
            System.out.println("Você depositou " + transicao + "reais.");
        }
    }

    public void sacar() {
          if (getSaldo() < 1 || getStatus() == false) {
            System.out.println("Para sacar, o saldo deve ser positivo e conta deve estar aberta.");
        }

        else {
            System.out.println("Você tem " + getSaldo() + " reais. Insira o valor a ser sacado:");
            this.transicao = scanner.nextFloat();
            if (transicao > getSaldo()) {
                System.out.println("Não é possível sacar um valor maior que o saldo.");
            }

            else {
                setSaldo(saldo - transicao);
                System.out.println("Você sacou " + transicao + "reais.");
            }
        }
    }

    public void pagarMensal() {
        if (getTipo() == "CC") {
            setSaldo(saldo - 12);
        }

        else {
                setSaldo(saldo - 20);
        }
    }
}
