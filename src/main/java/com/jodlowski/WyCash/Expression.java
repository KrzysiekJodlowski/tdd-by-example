package com.jodlowski.WyCash;

public interface Expression {
    Money reduce(Bank bank, String to);
}
