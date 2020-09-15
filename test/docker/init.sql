--
-- PostgreSQL database dump
--

-- Dumped from database version 10.6
-- Dumped by pg_dump version 10.12

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

SET default_tablespace = '';

SET default_with_oids = false;

--
-- Name: aquifers; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.aquifers (
    id integer NOT NULL,
    materials text,
    productivity text,
    vulnerability text,
    demand text,
    location_description text,
    url text,
    type_of_water_use text,
    geom public.geometry
);


ALTER TABLE public.aquifers OWNER TO postgres;

--
-- Name: aquifers_detail; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.aquifers_detail (
    id integer NOT NULL,
    materials text,
    productivity text,
    vulnerability text,
    demand text,
    location_description text,
    url text,
    type_of_water_use text,
    geom public.geometry
);


ALTER TABLE public.aquifers_detail OWNER TO postgres;

--
-- Name: aquifers_detail_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.aquifers_detail_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.aquifers_detail_id_seq OWNER TO postgres;

--
-- Name: aquifers_detail_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.aquifers_detail_id_seq OWNED BY public.aquifers_detail.id;


--
-- Name: aquifers_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.aquifers_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.aquifers_id_seq OWNER TO postgres;

--
-- Name: aquifers_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.aquifers_id_seq OWNED BY public.aquifers.id;


--
-- Name: culverts; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.culverts (
    id integer NOT NULL,
    name character varying,
    geom public.geometry(Point,4326)
);


ALTER TABLE public.culverts OWNER TO postgres;

--
-- Name: culverts_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.culverts_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.culverts_id_seq OWNER TO postgres;

--
-- Name: culverts_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.culverts_id_seq OWNED BY public.culverts.id;


-- noinspection SqlNoDataSourceInspection

CREATE TABLE public.field_observations (
    uuid uuid,
    coordinates public.geometry,
    flow_rate text,
    json_record json
);

ALTER TABLE public.field_observations OWNER TO postgres;
ALTER TABLE ONLY public.field_observations ADD CONSTRAINT field_observations_uuid_key UNIQUE (uuid);


--
-- Name: epicollect_observations; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.epicollect_observations (
    uuid uuid,
    created_by text,
    title text,
    location_name_desc text,
    general_island_area text,
    named_location_if_known text,
    watershed text[],
    describe_other_watershed text,
    where_am_i public.geometry,
    weather_check_all_that_apply text[],
    last_significant_precipitation_event text[],
    safe_to_work_at_this_location text[],
    name_initials_or_nickname text,
    no_of_participants integer,
    type_of_visit text[],
    general_land_use_in_area_to_25m text[],
    describe_other_land_use text,
    types_of_water_use text[],
    describe_other_water_use text,
    this_area_recieve text[],
    describe_other_drainage text,
    vegetation_in_area text[],
    canopy_coverage_within_5m text[],
    soil_rock_type text[],
    water_body_type text,
    water_body_name_if_known text,
    water_movement_visible text,
    likely_permenance text,
    flow_measurement_location text[],
    describe_other_fl text,
    wetted_width_m text,
    rate_of_flow_qualitative text,
    describe_water_level_qualitative text,
    method_of_measurement text,
    describe_other_measurement text,
    flow_rate_quantity_1 double precision,
    any_of_the_following_on_the_water_surface text[],
    type_of_algae_if_present text,
    evidence_of_aquatic_life text[],
    describe_other_incidental_species text,
    water_colour_hue text[],
    photo_view_upstr text,
    photo_view_downstream text,
    do_you_want_to_take_more_photos text[],
    additional_photo_1 text,
    additional_photo_2 text,
    are_you_taking_water_samples text,
    ph double precision,
    temperature double precision,
    conductivity double precision,
    other_comments text,
    water_matters text,
    created_at timestamp without time zone,
    flow_rate_quantity_2 double precision,
    flow_rate_quantity_3 double precision
);


ALTER TABLE public.epicollect_observations OWNER TO postgres;

--
-- Name: epicollect_observations_v2; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.epicollect_observations_v2 (
    uuid uuid,
    created_at text,
    created_by text,
    title text,
    locname text,
    i_am_a_hiker_walker text,
    date text,
    photo text,
    water_body_type text,
    water_movement text,
    brief_description text,
    should_ssifwc_visit text,
    island_area text,
    sub_loc_north text,
    sub_loc_central text,
    sub_loc_south text,
    other_loc_north text,
    other_loc_central text,
    other_loc_south text,
    coord public.geometry,
    date_2 text,
    time_2 text,
    temp text,
    cloud_cover text,
    precipitation text,
    last_sig_precipitation text,
    safe_to_work text,
    name text,
    number_of_participants text,
    water_moving text,
    flow_type text,
    visit_type text,
    gen_land_use text,
    other_land_use text,
    water_use text,
    other_water_use text,
    drainage_sources text,
    terrain text,
    water_level text,
    vegetation text,
    canopy_coverage text,
    surficial_geology text,
    water_surface text,
    algae text,
    algae_extent text,
    aquatic_life text,
    other_species text,
    absolute_depth_me text,
    describe_location text,
    describe_reference text,
    photo_of_water_le text,
    flow_measure text,
    flow_measure_loc text,
    current_wetted_wi text,
    estimated_wetted text,
    water_color text,
    water_turbitidy_q text,
    type_measure text,
    rate_of_flow text,
    describe_water_level text,
    method_measure text,
    simple_or_detailed text,
    measure_depth_cm text,
    distance_from_ban_1 text,
    depth_at_pt_1_cm text,
    distance_from_ban_2 text,
    depth_at_pt_2_cm text,
    distance_from_ban_3 text,
    depth_at_pt_3_cm text,
    distance_from_ban_4 text,
    depth_at_pt_4_cm text,
    distance_from_ban_5 text,
    depth_at_pt_5_cm text,
    distance_from_ban_6 text,
    depth_at_pt_6_cm text,
    distance_from_ban_7 text,
    depth_at_pt_7_cm text,
    distance_from_ban_8 text,
    depth_at_pt_8_cm text,
    distance_from_ban_9 text,
    depth_at_pt_9_cm text,
    distance_from_ban_10 text,
    depth_at_pt_10_cm text,
    quantitative_meas text,
    velocity_1_ms text,
    velocity_2_ms text,
    velocity_3_ms text,
    depth_to_meter_fr text,
    depth_from_meter text,
    enter_xsection_ar_1 text,
    distance_traveled text,
    time_1_sec text,
    time_2_sec text,
    time_3_sec text,
    enter_xsection_ar_2 text,
    flow_rate_average text,
    measurement_1_ls text,
    measurement_1_tim text,
    measurement_2_ls text,
    measurement_2_tim text,
    measurement_3_ls text,
    measurement_3_tim text,
    are_you_taking_ph text,
    photos text,
    photo_view_downst text,
    do_you_want_to_ta text,
    additional_photo_1 text,
    additional_photo_2 text,
    short_video text,
    are_you_taking_wa text,
    ph text,
    temperature text,
    conductivity text,
    total_dissolved text,
    dissolved_oxygen text,
    other_comments text,
    alkalinity text,
    hardness text
);


ALTER TABLE public.epicollect_observations_v2 OWNER TO postgres;

--
-- Name: faults; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.faults (
    id integer NOT NULL,
    name character varying,
    geom public.geometry(LineStringZ,4326)
);


ALTER TABLE public.faults OWNER TO postgres;

--
-- Name: faults_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.faults_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.faults_id_seq OWNER TO postgres;

--
-- Name: faults_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.faults_id_seq OWNED BY public.faults.id;


--
-- Name: geology; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.geology (
    id integer NOT NULL,
    name text,
    description text,
    geom public.geometry
);


ALTER TABLE public.geology OWNER TO postgres;

--
-- Name: geology_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.geology_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.geology_id_seq OWNER TO postgres;

--
-- Name: geology_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.geology_id_seq OWNED BY public.geology.id;


--
-- Name: greenwood; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.greenwood (
    id integer NOT NULL,
    geom public.geometry
);


ALTER TABLE public.greenwood OWNER TO postgres;

--
-- Name: greenwood_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.greenwood_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.greenwood_id_seq OWNER TO postgres;

--
-- Name: greenwood_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.greenwood_id_seq OWNED BY public.greenwood.id;


--
-- Name: parcel; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.parcel (
    id integer NOT NULL,
    geom public.geometry
);


ALTER TABLE public.parcel OWNER TO postgres;

--
-- Name: parcel_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.parcel_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.parcel_id_seq OWNER TO postgres;

--
-- Name: parcel_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.parcel_id_seq OWNED BY public.parcel.id;


--
-- Name: parcels; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.parcels (
    id integer NOT NULL,
    geom public.geometry
);


ALTER TABLE public.parcels OWNER TO postgres;

--
-- Name: parcels_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.parcels_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.parcels_id_seq OWNER TO postgres;

--
-- Name: parcels_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.parcels_id_seq OWNED BY public.parcels.id;


--
-- Name: spring; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.spring (
    id integer NOT NULL,
    stream_name text,
    purpose text,
    quantity double precision,
    units text,
    geom public.geometry
);


ALTER TABLE public.spring OWNER TO postgres;

--
-- Name: spring_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.spring_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.spring_id_seq OWNER TO postgres;

--
-- Name: spring_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.spring_id_seq OWNED BY public.spring.id;


--
-- Name: springs; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.springs (
    id integer NOT NULL,
    stream_name text,
    purpose text,
    quantity double precision,
    units text,
    geom public.geometry
);


ALTER TABLE public.springs OWNER TO postgres;

--
-- Name: springs_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.springs_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.springs_id_seq OWNER TO postgres;

--
-- Name: springs_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.springs_id_seq OWNED BY public.springs.id;


--
-- Name: stream_network; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.stream_network (
    id integer NOT NULL,
    name text,
    geom public.geometry
);


ALTER TABLE public.stream_network OWNER TO postgres;

--
-- Name: stream_network_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.stream_network_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.stream_network_id_seq OWNER TO postgres;

--
-- Name: stream_network_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.stream_network_id_seq OWNED BY public.stream_network.id;


--
-- Name: v_all_points; Type: VIEW; Schema: public; Owner: postgres
--

CREATE VIEW public.v_all_points AS
 SELECT epicollect_observations.uuid,
    epicollect_observations.where_am_i,
    epicollect_observations.created_at,
    epicollect_observations.temperature,
    epicollect_observations.conductivity,
    epicollect_observations.ph,
    (((epicollect_observations.flow_rate_quantity_1 + epicollect_observations.flow_rate_quantity_2) + epicollect_observations.flow_rate_quantity_3) / (3)::double precision) AS flow_rate,
    NULL::double precision AS alkalinity,
    NULL::double precision AS hardness,
    NULL::double precision AS dissolved_oxygen
   FROM public.epicollect_observations
UNION
 SELECT epicollect_observations_v2.uuid,
    epicollect_observations_v2.coord AS where_am_i,
    (epicollect_observations_v2.created_at)::timestamp without time zone AS created_at,
    (NULLIF(epicollect_observations_v2.temperature, ''::text))::double precision AS temperature,
    (NULLIF(epicollect_observations_v2.conductivity, ''::text))::double precision AS conductivity,
    (NULLIF(epicollect_observations_v2.ph, ''::text))::double precision AS ph,
    (NULLIF(epicollect_observations_v2.flow_rate_average, ''::text))::double precision AS flow_rate,
    (NULLIF(epicollect_observations_v2.alkalinity, ''::text))::double precision AS alkalinity,
    (NULLIF(epicollect_observations_v2.hardness, ''::text))::double precision AS hardness,
    (NULLIF(epicollect_observations_v2.dissolved_oxygen, ''::text))::double precision AS dissolved_oxygen
   FROM public.epicollect_observations_v2;


ALTER TABLE public.v_all_points OWNER TO postgres;

--
-- Name: watersheds_crd; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.watersheds_crd (
    id integer NOT NULL,
    name text,
    description text,
    geom public.geometry
);


ALTER TABLE public.watersheds_crd OWNER TO postgres;

--
-- Name: watersheds_crd_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.watersheds_crd_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.watersheds_crd_id_seq OWNER TO postgres;

--
-- Name: watersheds_crd_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.watersheds_crd_id_seq OWNED BY public.watersheds_crd.id;


--
-- Name: wells; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.wells (
    id integer NOT NULL,
    water_depth double precision,
    bedrock_depth double precision,
    elevation double precision,
    general_remarks text,
    yield_value double precision,
    url text,
    geom public.geometry
);


ALTER TABLE public.wells OWNER TO postgres;

--
-- Name: wells_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.wells_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.wells_id_seq OWNER TO postgres;

--
-- Name: wells_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.wells_id_seq OWNED BY public.wells.id;


--
-- Name: aquifers id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.aquifers ALTER COLUMN id SET DEFAULT nextval('public.aquifers_id_seq'::regclass);


--
-- Name: aquifers_detail id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.aquifers_detail ALTER COLUMN id SET DEFAULT nextval('public.aquifers_detail_id_seq'::regclass);


--
-- Name: culverts id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.culverts ALTER COLUMN id SET DEFAULT nextval('public.culverts_id_seq'::regclass);


--
-- Name: faults id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.faults ALTER COLUMN id SET DEFAULT nextval('public.faults_id_seq'::regclass);


--
-- Name: geology id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.geology ALTER COLUMN id SET DEFAULT nextval('public.geology_id_seq'::regclass);


--
-- Name: greenwood id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.greenwood ALTER COLUMN id SET DEFAULT nextval('public.greenwood_id_seq'::regclass);


--
-- Name: parcel id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.parcel ALTER COLUMN id SET DEFAULT nextval('public.parcel_id_seq'::regclass);


--
-- Name: parcels id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.parcels ALTER COLUMN id SET DEFAULT nextval('public.parcels_id_seq'::regclass);


--
-- Name: spring id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.spring ALTER COLUMN id SET DEFAULT nextval('public.spring_id_seq'::regclass);


--
-- Name: springs id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.springs ALTER COLUMN id SET DEFAULT nextval('public.springs_id_seq'::regclass);


--
-- Name: stream_network id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.stream_network ALTER COLUMN id SET DEFAULT nextval('public.stream_network_id_seq'::regclass);


--
-- Name: watersheds_crd id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.watersheds_crd ALTER COLUMN id SET DEFAULT nextval('public.watersheds_crd_id_seq'::regclass);


--
-- Name: wells id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.wells ALTER COLUMN id SET DEFAULT nextval('public.wells_id_seq'::regclass);


--
-- Name: epicollect_observations epicollect_observations_uuid_key; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.epicollect_observations
    ADD CONSTRAINT epicollect_observations_uuid_key UNIQUE (uuid);


--
-- Name: epicollect_observations_v2 epicollect_observations_v2_uuid_key; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.epicollect_observations_v2
    ADD CONSTRAINT epicollect_observations_v2_uuid_key UNIQUE (uuid);


--
-- Name: SCHEMA public; Type: ACL; Schema: -; Owner: postgres
--

REVOKE ALL ON SCHEMA public FROM PUBLIC;
GRANT ALL ON SCHEMA public TO postgres;
GRANT ALL ON SCHEMA public TO PUBLIC;


--
-- PostgreSQL database dump complete
--

