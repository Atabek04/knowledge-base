
## Why we decided to use ClickHouse

showing when it shines over PG

## Why we have Dual-Writing

Question to resolve: why writing to PG isn't enough
and is it only because CH may not work, when you get new data from SOAP, and u might lose those data? and so u want to store them in PG as well

## Why we need to use Outbox Pattern (aka Debezium)

showing its importance and also difference between Outbox and Debezium