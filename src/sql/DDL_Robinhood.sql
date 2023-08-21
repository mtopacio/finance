CREATE TABLE IF NOT EXISTS instruments(
    "symbol" TEXT PRIMARY KEY,
    "simple_name" TEXT,
    "name" TEXT,
    "list_date" DATE,
    "type" TEXT,
    "id" UUID,
    "tradable_chain_id" TEXT,
    "rhs_tradability" BOOLEAN,
    "fractional_tradability" BOOLEAN,
    "date_added" DATE DEFAULT NOW(),
    "date_updated" DATE DEFAULT NOW(),
    FOREIGN KEY (symbol) REFERENCES focus(symbol)
);

CREATE TABLE IF NOT EXISTS watchlists(
    "symbol" TEXT PRIMARY KEY,
    "date_added" DATE DEFAULT now(),
    "date_delete" DATE DEFAULT NULL
)

CREATE TABLE IF NOT EXISTS historicals(
    "symbol" TEXT PRIMARY KEY,
    "date" DATE NOT NULL,
    "open" NUMERIC(12,2) NOT NULL,
    "high" NUMERIC(12,2) NOT NULL,
    "low" NUMERIC(12,2) NOT NULL,
    "close" NUMERIC(12,2) NOT NULL,
    "volume" BIGINT NOT NULL,
    FOREIGN KEY (symbol) REFERENCES instruments(symbol)
        ON DELETE DO NOTHING;
);

CREATE TABLE IF NOT EXISTS account(
    "start_date" DATE,
    market_value NUMERIC(12,2),
    equity NUMERIC(12,2),
    excess_margin NUMERIC(12,2),
    excess_maintenance NUMERIC(12,2),
    excess_margin_with_uncleared_deposits NUMERIC(12,2),
    excess_maintenance_with_uncleared_deposits NUMERIC(12,2)
    equity_previous_close NUMERIC(12,2),
    withdrawable_amount NUMERIC(12,2)
);

CREATE TABLE IF NOT EXISTS orders(
    id UUID, 
    ref_id UUID,
    symbol,
    cum_qty numeric(12,4), 
    avg_price numeric(12,4),
    fees numeric()
);

CREATE TABLE IF NOT EXISTS calendar