public enum TipoPagamento {
    DEBITO {
        @Override
        public double cancularDesconto(double valor) {
        return valor * 0.1;
    }
    }, 
    CREDITO {
        @Override
        public double cancularDesconto(double valor) {
        return valor * 0.05;
    }
    };

    public abstract double cancularDesconto(double valor);
}
