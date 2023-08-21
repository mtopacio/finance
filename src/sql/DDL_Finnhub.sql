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

CREATE TABLE IF NOT EXISTS sentiment(
    "symbol" TEXT PRIMARY KEY,
    "datetime" TIMESTAMPTZ,
    "mention" INTEGER,
    "positive_score" NUMERIC,
    "negative_score" NUMERIC,
    "positive_mention" INTEGER,
    "negative_mention" INTEGER,
    "score" INTEGER,
    FOREIGN KEY ("symbol") REFERENCES instruments("symbol")
)

CREATE TABLE IF NOT EXISTS