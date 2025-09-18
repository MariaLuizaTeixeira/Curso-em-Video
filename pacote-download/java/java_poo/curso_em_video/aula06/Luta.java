package aula06;

import java.util.Random;

public class Luta {
    // Atributos
    private Lutador desafiado;
    private Lutador desafiante;
    private int rounds;
    private boolean aprovada;

    // Construtor
    public Luta() {
    }

    // Getters e setters
    public Lutador getDesafiado() {
        return desafiado;
    }

    public void setDesafiado(Lutador dd) {
        this.desafiado = dd;
    }

    public Lutador getdesafiante() {
        return desafiante;
    }

    public void setdesafiante(Lutador desafiante) {
        this.desafiante = desafiante;
    }

    public int getRounds() {
        return rounds;
    }

    public void setRounds(int rounds) {
        this.rounds = rounds;
    }

    public boolean isAprovada() {
        return aprovada;
    }

    public void setAprovada(boolean aprovada) {
        this.aprovada = aprovada;
    }

    // Métodos
    public void marcarLuta(Lutador l1, Lutador l2) {
        if (l1.getCategoria() == l2.getCategoria() && l1 != l2) {
            setAprovada(true);
            setDesafiado(l1);
            setdesafiante(l2);
        }

        else {
            setAprovada(false);
            setDesafiado(null);
            setdesafiante(null);
        }
    }

    public void lutar() {
        if (isAprovada() == true) {
            desafiado.apresentar();
            desafiante.apresentar();

            Random aleatorio = new Random();
            int vencedor = aleatorio.nextInt(3);

            switch (vencedor) {
                case 0:
                System.out.println("Empate.");
                    this.desafiado.empatarLuta();
                    this.desafiante.empatarLuta();
                    break;
                case 1:
                    System.out.println("Desafiante ganhou!");
                    this.desafiante.ganharLuta();
                    this.desafiado.perderLuta();
                    break;
                case 2:
                    System.out.println("Desafiado ganhou!");
                    this.desafiante.perderLuta();
                    this.desafiado.ganharLuta();
                    break;
                default:
                    break;
            }
        }

        else {
            System.out.println("Luta não pode acontecer.");
        }
    }
}
