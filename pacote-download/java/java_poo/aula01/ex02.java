package aula01;
public class ex02 {
    public static void main(String[] args) {
        Trabalho t1 = new Trabalho();
        t1.data_entrada = "2024-08-18";
        t1.funcao = "Estagiária";
        t1.horas_semanais = 20;
        t1.no_trabalho = true;
        t1.salario = 698;
        t1.chegar();
        t1.sair();
        t1.trabalhar();
    }
}
