package aula01;
public class ex01 {
    public static void main(String[] args) {
        Televisao tv1 = new Televisao();
        tv1.ano_producao = 2025;
        tv1.ano_validade = 2030;
        tv1.cor = "Preta";
        tv1.marca = "Samsung";
        tv1.polegadas = 300;
        tv1.resolucao = 100000;
        tv1.ligada = true;

        tv1.desligar();
        tv1.ligar();
        tv1.mudar_canal();
    }
}
