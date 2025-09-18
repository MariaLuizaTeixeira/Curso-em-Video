package aula05;

public class ControleRemoto implements Controlador {
    // Atributos
    private int volume;
    private boolean ligado;
    private boolean tocando;

    // Getters e Setters
    private int getVolume() {
        return volume;
    }

    private void setVolume(int volume) {
        this.volume = volume;
    }

    private boolean isLigado() {
        return ligado;
    }

    private void setLigado(boolean ligado) {
        this.ligado = ligado;
    }

    private boolean isTocando() {
        return tocando;
    }

    private void setTocando(boolean tocando) {
        this.tocando = tocando;
    }

    public ControleRemoto() {
        this.volume = 50;
        this.ligado = false;
        this.tocando = false;
    }

    @Override
    public void ligar() {
        this.setLigado(true);
        this.setTocando(true);
    }

    @Override
    public void desligar() {
        this.setLigado(false);
    }

    @Override
    public void abrirMenu() {
        System.out.println("Está ligado? " + this.isLigado());
        System.out.println("Está tocando? " + this.isTocando());
        System.out.print("Volume: " + this.getVolume());
        for (int i = 0; i <= this.getVolume(); i+=10) {
            System.out.print(" | ");
        }
        System.err.println();
    }

    @Override
    public void fecharMenu() {
        System.out.println("Fechando menu...");
    }

    @Override
    public void maisVolume() {
        if (this.isLigado() == true) {
            this.setVolume(this.getVolume() + 1);
        }
    }

    @Override
    public void menosVolume() {
        if (this.isLigado() == true) {
            this.setVolume(this.getVolume() - 1);
        }
    }

    @Override
    public void ligarMudo() {
        if (this.isLigado() == true && this.getVolume() > 0) {
            this.setVolume(0);
        }
    }

    @Override
    public void desligarMudo() {
        if (this.isLigado() == true && this.getVolume() == 0) {
            this.setVolume(50);
        }
    }

    @Override
    public void play() {
        if (this.isLigado() == true && !(this.isTocando() == true)) {
            this.setTocando(true);
        }
    }

    @Override
    public void pause() {
        if (this.isLigado() == true && this.isTocando() == true) {
            this.setTocando(false);
        }
    }

}
