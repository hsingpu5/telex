create table table_name
(
    id          NUMBER(12),
    text        VARCHAR2 (255 CHAR) not null, --char类型,一个汉字占一个长度
    PID         VARCHAR2 (32 BYTE) NOT NULL,  --byte类型,UTF8一个汉字占大约两个长度
    status      NUMBER(1) DEFAULT 0 null,    --添加默认值 如果为空默认值就为0
    phoneNumber NUMBER(11),
    cash        BINARY_FLOAT(6),
    info        TIMESTAMP (12)
)
--添加主键
ALTER TABLE "test"."table_name"
    ADD PRIMARY KEY ("ID");

--添加注释
comment
on column table_name.id is '主键';
    comment
on column table_name.text is '说明';
    comment
on column table_name.status is '状态';
