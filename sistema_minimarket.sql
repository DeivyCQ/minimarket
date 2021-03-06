PGDMP     	                	    x            sex_shop    12.4    12.4 -    P           0    0    ENCODING    ENCODING        SET client_encoding = 'UTF8';
                      false            Q           0    0 
   STDSTRINGS 
   STDSTRINGS     (   SET standard_conforming_strings = 'on';
                      false            R           0    0 
   SEARCHPATH 
   SEARCHPATH     8   SELECT pg_catalog.set_config('search_path', '', false);
                      false            S           1262    32768    sex_shop    DATABASE     �   CREATE DATABASE sex_shop WITH TEMPLATE = template0 ENCODING = 'UTF8' LC_COLLATE = 'Spanish_Peru.1252' LC_CTYPE = 'Spanish_Peru.1252';
    DROP DATABASE sex_shop;
                postgres    false            �            1259    32787 	   categoria    TABLE     p   CREATE TABLE public.categoria (
    id_descripcion smallint NOT NULL,
    descripcion character(50) NOT NULL
);
    DROP TABLE public.categoria;
       public         heap    postgres    false            �            1259    32894    cierre_caja    TABLE     �   CREATE TABLE public.cierre_caja (
    id_caja integer NOT NULL,
    fecha date NOT NULL,
    id_usuario smallint NOT NULL,
    importe numeric
);
    DROP TABLE public.cierre_caja;
       public         heap    postgres    false            �            1259    32807    compra_cabecera    TABLE     �   CREATE TABLE public.compra_cabecera (
    id_comp_cabecera integer NOT NULL,
    tipo character(4),
    comprobante character(1),
    fecha date,
    precio numeric NOT NULL
);
 #   DROP TABLE public.compra_cabecera;
       public         heap    postgres    false            �            1259    32833    compra_detalle    TABLE     %  CREATE TABLE public.compra_detalle (
    id_comp_detalle integer NOT NULL,
    posicion smallint NOT NULL,
    id_producto integer,
    descripcion character(100),
    cantidad numeric(10,3),
    unidad_medida character(3),
    precio_unitario numeric(10,2),
    precio_total numeric(10,2)
);
 "   DROP TABLE public.compra_detalle;
       public         heap    postgres    false            �            1259    32792    marca    TABLE     ]   CREATE TABLE public.marca (
    id_marca smallint NOT NULL,
    descripcion character(50)
);
    DROP TABLE public.marca;
       public         heap    postgres    false            �            1259    32797    producto    TABLE     0  CREATE TABLE public.producto (
    id_producto integer NOT NULL,
    descripcion character(100) NOT NULL,
    id_categoria smallint NOT NULL,
    id_marca smallint NOT NULL,
    stock numeric(10,3),
    precio numeric(10,2),
    unidad_medida_compra character(3),
    unidad_medida_venta character(3)
);
    DROP TABLE public.producto;
       public         heap    postgres    false            �            1259    32771    rol    TABLE     b   CREATE TABLE public.rol (
    id_rol smallint NOT NULL,
    descripcion character(50) NOT NULL
);
    DROP TABLE public.rol;
       public         heap    postgres    false            �            1259    32769    rol_id_rol_seq    SEQUENCE     �   CREATE SEQUENCE public.rol_id_rol_seq
    AS smallint
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 %   DROP SEQUENCE public.rol_id_rol_seq;
       public          postgres    false    203            T           0    0    rol_id_rol_seq    SEQUENCE OWNED BY     A   ALTER SEQUENCE public.rol_id_rol_seq OWNED BY public.rol.id_rol;
          public          postgres    false    202            �            1259    32802    tipo_compra    TABLE     h   CREATE TABLE public.tipo_compra (
    id_tip_compra smallint NOT NULL,
    descripcion character(50)
);
    DROP TABLE public.tipo_compra;
       public         heap    postgres    false            �            1259    32777    usuario    TABLE     �   CREATE TABLE public.usuario (
    id_usuario smallint NOT NULL,
    id_rol smallint NOT NULL,
    nombre character(120),
    nombre_usuario character(20),
    correo character(50)
);
    DROP TABLE public.usuario;
       public         heap    postgres    false            �            1259    32846    venta_cabecera    TABLE     �   CREATE TABLE public.venta_cabecera (
    id_vent_cabecera integer NOT NULL,
    tipo character(4),
    comprobante character(20),
    fecha date,
    precio numeric(10,2)
);
 "   DROP TABLE public.venta_cabecera;
       public         heap    postgres    false            �            1259    32884    venta_detalle    TABLE     $  CREATE TABLE public.venta_detalle (
    id_vent_detalle integer NOT NULL,
    posicion smallint NOT NULL,
    id_producto integer,
    descripcion character(100),
    cantidad numeric(10,3),
    unidad_medida character(3),
    precio_unitario numeric(10,2),
    precio_total numeric(10,2)
);
 !   DROP TABLE public.venta_detalle;
       public         heap    postgres    false            �
           2604    32774 
   rol id_rol    DEFAULT     h   ALTER TABLE ONLY public.rol ALTER COLUMN id_rol SET DEFAULT nextval('public.rol_id_rol_seq'::regclass);
 9   ALTER TABLE public.rol ALTER COLUMN id_rol DROP DEFAULT;
       public          postgres    false    203    202    203            E          0    32787 	   categoria 
   TABLE DATA           @   COPY public.categoria (id_descripcion, descripcion) FROM stdin;
    public          postgres    false    205   Q4       M          0    32894    cierre_caja 
   TABLE DATA           J   COPY public.cierre_caja (id_caja, fecha, id_usuario, importe) FROM stdin;
    public          postgres    false    213   n4       I          0    32807    compra_cabecera 
   TABLE DATA           ]   COPY public.compra_cabecera (id_comp_cabecera, tipo, comprobante, fecha, precio) FROM stdin;
    public          postgres    false    209   �4       J          0    32833    compra_detalle 
   TABLE DATA           �   COPY public.compra_detalle (id_comp_detalle, posicion, id_producto, descripcion, cantidad, unidad_medida, precio_unitario, precio_total) FROM stdin;
    public          postgres    false    210   �4       F          0    32792    marca 
   TABLE DATA           6   COPY public.marca (id_marca, descripcion) FROM stdin;
    public          postgres    false    206   �4       G          0    32797    producto 
   TABLE DATA           �   COPY public.producto (id_producto, descripcion, id_categoria, id_marca, stock, precio, unidad_medida_compra, unidad_medida_venta) FROM stdin;
    public          postgres    false    207   �4       C          0    32771    rol 
   TABLE DATA           2   COPY public.rol (id_rol, descripcion) FROM stdin;
    public          postgres    false    203   �4       H          0    32802    tipo_compra 
   TABLE DATA           A   COPY public.tipo_compra (id_tip_compra, descripcion) FROM stdin;
    public          postgres    false    208   5       D          0    32777    usuario 
   TABLE DATA           U   COPY public.usuario (id_usuario, id_rol, nombre, nombre_usuario, correo) FROM stdin;
    public          postgres    false    204   95       K          0    32846    venta_cabecera 
   TABLE DATA           \   COPY public.venta_cabecera (id_vent_cabecera, tipo, comprobante, fecha, precio) FROM stdin;
    public          postgres    false    211   V5       L          0    32884    venta_detalle 
   TABLE DATA           �   COPY public.venta_detalle (id_vent_detalle, posicion, id_producto, descripcion, cantidad, unidad_medida, precio_unitario, precio_total) FROM stdin;
    public          postgres    false    212   s5       U           0    0    rol_id_rol_seq    SEQUENCE SET     =   SELECT pg_catalog.setval('public.rol_id_rol_seq', 1, false);
          public          postgres    false    202            �
           2606    32791    categoria categoria_pkey 
   CONSTRAINT     b   ALTER TABLE ONLY public.categoria
    ADD CONSTRAINT categoria_pkey PRIMARY KEY (id_descripcion);
 B   ALTER TABLE ONLY public.categoria DROP CONSTRAINT categoria_pkey;
       public            postgres    false    205            �
           2606    32901    cierre_caja cierre_caja_pkey 
   CONSTRAINT     _   ALTER TABLE ONLY public.cierre_caja
    ADD CONSTRAINT cierre_caja_pkey PRIMARY KEY (id_caja);
 F   ALTER TABLE ONLY public.cierre_caja DROP CONSTRAINT cierre_caja_pkey;
       public            postgres    false    213            �
           2606    32814 $   compra_cabecera compra_cabecera_pkey 
   CONSTRAINT     p   ALTER TABLE ONLY public.compra_cabecera
    ADD CONSTRAINT compra_cabecera_pkey PRIMARY KEY (id_comp_cabecera);
 N   ALTER TABLE ONLY public.compra_cabecera DROP CONSTRAINT compra_cabecera_pkey;
       public            postgres    false    209            �
           2606    32840 "   compra_detalle compra_detalle_pkey 
   CONSTRAINT     m   ALTER TABLE ONLY public.compra_detalle
    ADD CONSTRAINT compra_detalle_pkey PRIMARY KEY (id_comp_detalle);
 L   ALTER TABLE ONLY public.compra_detalle DROP CONSTRAINT compra_detalle_pkey;
       public            postgres    false    210            �
           2606    32796    marca marca_pkey 
   CONSTRAINT     T   ALTER TABLE ONLY public.marca
    ADD CONSTRAINT marca_pkey PRIMARY KEY (id_marca);
 :   ALTER TABLE ONLY public.marca DROP CONSTRAINT marca_pkey;
       public            postgres    false    206            �
           2606    32801    producto producto_pkey 
   CONSTRAINT     ]   ALTER TABLE ONLY public.producto
    ADD CONSTRAINT producto_pkey PRIMARY KEY (id_producto);
 @   ALTER TABLE ONLY public.producto DROP CONSTRAINT producto_pkey;
       public            postgres    false    207            �
           2606    32776    rol rol_pkey 
   CONSTRAINT     N   ALTER TABLE ONLY public.rol
    ADD CONSTRAINT rol_pkey PRIMARY KEY (id_rol);
 6   ALTER TABLE ONLY public.rol DROP CONSTRAINT rol_pkey;
       public            postgres    false    203            �
           2606    32806    tipo_compra tipo_compra_pkey 
   CONSTRAINT     e   ALTER TABLE ONLY public.tipo_compra
    ADD CONSTRAINT tipo_compra_pkey PRIMARY KEY (id_tip_compra);
 F   ALTER TABLE ONLY public.tipo_compra DROP CONSTRAINT tipo_compra_pkey;
       public            postgres    false    208            �
           2606    32781    usuario usuario_pkey 
   CONSTRAINT     Z   ALTER TABLE ONLY public.usuario
    ADD CONSTRAINT usuario_pkey PRIMARY KEY (id_usuario);
 >   ALTER TABLE ONLY public.usuario DROP CONSTRAINT usuario_pkey;
       public            postgres    false    204            �
           2606    32850 "   venta_cabecera venta_cabecera_pkey 
   CONSTRAINT     n   ALTER TABLE ONLY public.venta_cabecera
    ADD CONSTRAINT venta_cabecera_pkey PRIMARY KEY (id_vent_cabecera);
 L   ALTER TABLE ONLY public.venta_cabecera DROP CONSTRAINT venta_cabecera_pkey;
       public            postgres    false    211            �
           2606    32888     venta_detalle venta_detalle_pkey 
   CONSTRAINT     k   ALTER TABLE ONLY public.venta_detalle
    ADD CONSTRAINT venta_detalle_pkey PRIMARY KEY (id_vent_detalle);
 J   ALTER TABLE ONLY public.venta_detalle DROP CONSTRAINT venta_detalle_pkey;
       public            postgres    false    212            �
           2606    32841    compra_detalle compra_cabecera    FK CONSTRAINT     �   ALTER TABLE ONLY public.compra_detalle
    ADD CONSTRAINT compra_cabecera FOREIGN KEY (id_comp_detalle) REFERENCES public.compra_cabecera(id_comp_cabecera);
 H   ALTER TABLE ONLY public.compra_detalle DROP CONSTRAINT compra_cabecera;
       public          postgres    false    209    2743    210            �
           2606    32782    usuario id_rol    FK CONSTRAINT     n   ALTER TABLE ONLY public.usuario
    ADD CONSTRAINT id_rol FOREIGN KEY (id_rol) REFERENCES public.rol(id_rol);
 8   ALTER TABLE ONLY public.usuario DROP CONSTRAINT id_rol;
       public          postgres    false    2731    203    204            �
           2606    32902    cierre_caja usuario    FK CONSTRAINT        ALTER TABLE ONLY public.cierre_caja
    ADD CONSTRAINT usuario FOREIGN KEY (id_usuario) REFERENCES public.usuario(id_usuario);
 =   ALTER TABLE ONLY public.cierre_caja DROP CONSTRAINT usuario;
       public          postgres    false    204    213    2733            �
           2606    32889    venta_detalle venta_cabecera    FK CONSTRAINT     �   ALTER TABLE ONLY public.venta_detalle
    ADD CONSTRAINT venta_cabecera FOREIGN KEY (id_vent_detalle) REFERENCES public.venta_cabecera(id_vent_cabecera);
 F   ALTER TABLE ONLY public.venta_detalle DROP CONSTRAINT venta_cabecera;
       public          postgres    false    211    2747    212            E      x������ � �      M      x������ � �      I      x������ � �      J      x������ � �      F      x������ � �      G      x������ � �      C      x������ � �      H      x������ � �      D      x������ � �      K      x������ � �      L      x������ � �     