# -*- coding: utf-8 -*-
from peewee import *
from peewee_async import MySQLDatabase, Manager

db = MySQLDatabase(None)
db_manager = Manager(db)


class BaseModel(Model):
    class Meta:
        database = db


class Administrator(BaseModel):
    corporation = CharField()
    email = CharField()
    login = CharField(unique=True)
    mobile = CharField()
    name = CharField()
    password = CharField()
    phone = CharField()
    source = IntegerField(db_column='source_id', null=True)
    type = CharField()
    valid = IntegerField()

    class Meta:
        db_table = 'T_ADMINISTRATOR'


class AdministratorLoginLog(BaseModel):
    administrator_id = IntegerField()
    id = BigIntegerField(primary_key=True)
    source = CharField()
    timestamp = BigIntegerField()

    class Meta:
        db_table = 'T_ADMINISTRATOR_LOGIN_LOG'


class AdministratorSource(BaseModel):
    name = CharField(unique=True)

    class Meta:
        db_table = 'T_ADMINISTRATOR_SOURCE'


class AlarmContact(BaseModel):
    email = CharField(null=True)
    id = BigIntegerField(primary_key=True)
    mobile = CharField(null=True)
    tid = CharField(null=True, unique=True)

    class Meta:
        db_table = 'T_ALARM_CONTACT'


class AlarmSmsNotifications(BaseModel):
    heartbeat_lost = IntegerField(null=True)
    illegalmove = IntegerField(null=True)
    illegalshake = IntegerField(null=True)
    overspeed = IntegerField(null=True)
    poi = IntegerField(null=True)
    powerfull = IntegerField(null=True)
    powerlow = IntegerField(null=True)
    poweroff = IntegerField(null=True)
    region = IntegerField(null=True)
    sos = IntegerField(null=True)
    stopping = IntegerField(null=True)
    temp = IntegerField(null=True)
    tid = CharField(null=True)
    usb_disconnect = IntegerField(null=True)

    class Meta:
        db_table = 'T_ALARM_SMS_NOTIFICATIONS'


class AlarmVoiceNotifications(BaseModel):
    heartbeat_lost = IntegerField(null=True)
    illegalmove = IntegerField(null=True)
    illegalshake = IntegerField(null=True)
    overspeed = IntegerField(null=True)
    poi = IntegerField(null=True)
    powerfull = IntegerField(null=True)
    powerlow = IntegerField(null=True)
    poweroff = IntegerField(null=True)
    region = IntegerField(null=True)
    sos = IntegerField(null=True)
    stopping = IntegerField(null=True)
    temp = IntegerField(null=True)
    tid = CharField(null=True)
    usb_disconnect = IntegerField(null=True)

    class Meta:
        db_table = 'T_ALARM_VOICE_NOTIFICATIONS'


class AreaPrivilege(BaseModel):
    administrator = ForeignKeyField(db_column='administrator_id',
                                    rel_model=Administrator, to_field='id')
    area = IntegerField(db_column='area_id')
    category = IntegerField()

    class Meta:
        db_table = 'T_AREA_PRIVILEGE'


class Attention(BaseModel):
    id = IntegerField()
    event_time = IntegerField(null=True)
    lid = BigIntegerField(null=True)
    tid = CharField()
    type = IntegerField(null=True)

    class Meta:
        db_table = 'T_ATTENTION'
        indexes = (
            (('tid', 'event_time'), False),
        )


class TerminalInfo(BaseModel):
    activation_code = CharField()
    agent = BigIntegerField()
    agent_id = BigIntegerField()
    agps = CharField(null=True)
    alias = CharField(null=True)
    begintime = BigIntegerField()
    cellid_status = IntegerField(null=True)
    charging_status = IntegerField()
    defend_status = IntegerField(null=True)
    destination_range = IntegerField(null=True)
    dev_type = IntegerField(null=True)
    domain = CharField()
    endtime = BigIntegerField()
    factory_name = CharField(null=True)
    fob_status = IntegerField(null=True)
    freq = IntegerField()
    gps = IntegerField(null=True)
    gsm = IntegerField(null=True)
    heartbeat_interval = IntegerField(null=True)
    high_resolution = IntegerField()
    iccid = CharField(null=True)
    icon = IntegerField()
    id = BigIntegerField(primary_key=True)
    is_moving = IntegerField()
    keys_num = IntegerField()
    login = IntegerField()
    login_time = BigIntegerField()
    mannual_status = IntegerField()
    marker = IntegerField()
    mobile = CharField()
    mode = IntegerField()
    model = IntegerField()
    model_name = CharField(null=True)
    moving_threshold = CharField(null=True)
    msgid = IntegerField(null=True)
    operator = CharField(null=True)
    pbat = IntegerField(null=True)
    pulse = IntegerField(null=True)
    push_status = IntegerField(null=True)
    pvt_buffer_time = IntegerField(null=True)
    reboot = IntegerField()
    scriptversion = CharField(null=True)
    service_status = IntegerField(null=True)
    sn = CharField(null=True)
    softversion = CharField(null=True)
    sos_pop = IntegerField(null=True)
    stop_threshold = IntegerField(null=True)
    temp = IntegerField()
    tid = CharField(unique=True)
    trace = IntegerField(null=True)
    trace_para = CharField()
    track = IntegerField()
    uid = CharField(index=True, null=True)
    update_interval = CharField(null=True)
    update_time = BigIntegerField()
    vibchk = CharField(null=True)
    vibl = IntegerField(null=True)
    vibration_interruption = CharField(null=True)
    vibration_sensitivity = IntegerField(null=True)

    class Meta:
        db_table = 'T_TERMINAL_INFO'


class Car(BaseModel):
    brand = CharField(null=True)
    cid = BigIntegerField(index=True, null=True)
    cnum = CharField(null=True)
    color = CharField(null=True)
    fuel_city = FloatField(default=9.)
    fuel_highway = FloatField(default=7.)
    group = IntegerField(db_column='group_id', null=True)
    id = BigIntegerField(primary_key=True)
    idle_time_switch = IntegerField(db_column='idle_time', null=True)
    max_temp = FloatField(null=True)
    min_temp = FloatField(null=True)
    speed_limit = IntegerField(default=120)
    fuel_switch = IntegerField(db_column='switch', null=True)
    tid = ForeignKeyField(db_column='tid', rel_model=TerminalInfo,
                          to_field='tid', unique=True)
    type = IntegerField(null=True)

    class Meta:
        db_table = 'T_CAR'


class Carrier(BaseModel):
    carrier_name = CharField()
    country = CharField()
    id = BigIntegerField(primary_key=True)
    mail_server = CharField()

    class Meta:
        db_table = 'T_CARRIER'


class CarEqp(BaseModel):
    add_time = BigIntegerField(null=True)
    alert = IntegerField(null=True)
    eqp_id = IntegerField(db_column='eqp_id')
    eqp_name = CharField(null=True)
    id = BigIntegerField(primary_key=True)
    mac_addr = CharField(null=True)
    max_temp = FloatField(null=True)
    min_temp = FloatField(null=True)
    tid = CharField(index=True)
    value = FloatField(null=True)

    class Meta:
        db_table = 'T_CAR_EQP'


class CarEqpData(BaseModel):
    id = BigIntegerField(primary_key=True)
    tid = CharField(null=True)
    timestamp = BigIntegerField(null=True)
    type = CharField(null=True)
    value_digit = FloatField(null=True)
    value_text = CharField(null=True)

    class Meta:
        db_table = 'T_CAR_EQP_DATA'
        indexes = (
            (('tid', 'timestamp'), False),
        )


class CarSource(BaseModel):
    category = IntegerField()
    class_ = CharField(db_column='class')
    comment = CharField()
    fuel_city = IntegerField()
    fuel_combined = IntegerField()
    fuel_highway = IntegerField()
    html = CharField()
    icon_path = CharField()
    id = BigIntegerField(primary_key=True)
    make = CharField()
    model = CharField()
    mpge_city = IntegerField()
    mpge_combined = IntegerField()
    mpge_highway = IntegerField()
    year = CharField()

    class Meta:
        db_table = 'T_CAR_SOURCE'


class CellInfo(BaseModel):
    cell = CharField(null=True)
    ggp = CharField(null=True)
    id = BigIntegerField(primary_key=True)
    ncell = IntegerField(null=True)
    nwifi = IntegerField(null=True)
    scell = CharField(null=True)
    temp = IntegerField(null=True)
    tid = CharField(index=True, null=True)
    timestamp = BigIntegerField(index=True, null=True)
    wifi = CharField(null=True)

    class Meta:
        db_table = 'T_CELL_INFO'


class Charge(BaseModel):
    content = TextField(null=True)
    id = BigIntegerField(primary_key=True)
    tid = CharField()
    timestamp = BigIntegerField(null=True)

    class Meta:
        db_table = 'T_CHARGE'


class CodeVersion(BaseModel):
    category = IntegerField(null=True)
    version = CharField(null=True)

    class Meta:
        db_table = 'T_CODE_VERSION'


class Company(BaseModel):
    class Meta:
        db_table = 'T_COMPANY'


class Country(BaseModel):
    country = CharField(db_column='country_id', null=True)
    country_name = CharField(null=True)

    class Meta:
        db_table = 'T_COUNTRY'


class CountryCode(BaseModel):
    country = CharField(null=True)
    call_prefix = CharField(null=True)

    class Meta:
        db_table = 'T_COUNTRY_CODE'


class Current(BaseModel):
    choose_type = IntegerField()
    current_drivingtime = BigIntegerField(null=True)
    current_drivingtime_time = BigIntegerField(null=True)
    current_mileage = FloatField(null=True)
    current_mileage_time = BigIntegerField(null=True)
    flag = IntegerField(null=True)
    id = BigIntegerField(primary_key=True)
    init_drivingtime = BigIntegerField(null=True)
    init_drivingtime_time = BigIntegerField(null=True)
    init_mileage = FloatField(null=True)
    init_mileage_time = BigIntegerField(null=True)
    tid = CharField(null=True)

    class Meta:
        db_table = 'T_CURRENT'


class DbjayOrdernumSeq(BaseModel):
    class Meta:
        db_table = 'T_DBJAY_ORDERNUM_SEQ'


class DbjtechOrdernumSeq(BaseModel):
    class Meta:
        db_table = 'T_DBJTECH_ORDERNUM_SEQ'


class User(BaseModel):

    FIELED_ALIASES = [('mobile', 'phone'),
                      ('carrier_id', 'carrier'),
                      ('name', 'first_name')]

    activate_time = IntegerField(null=True)
    address = CharField(null=True)
    address2 = CharField(null=True)
    agent_id = IntegerField()
    avatar = CharField()
    billing_email = CharField(null=True)
    birthday = CharField()
    carrier = BigIntegerField(db_column='carrier_id')
    city = CharField(null=True)
    company = CharField(null=True)
    company_id = IntegerField(null=True)
    country = CharField(null=True)
    date_format = IntegerField(null=True)
    email = CharField(null=True)
    is_admin = IntegerField()
    language = IntegerField()
    last_name = CharField(null=True)
    login = IntegerField()
    phone = CharField(db_column='mobile', null=True)
    first_name = CharField(db_column='name', null=True)
    password = CharField(null=True)
    postalcode = CharField(null=True)
    province = CharField(null=True)
    register_time = IntegerField(null=True)
    remark = CharField(null=True)
    role_id = IntegerField(db_column='role_id', null=True)
    sanswer = CharField()
    squestion = CharField()
    status = IntegerField()
    time_format = IntegerField()
    timezone = IntegerField()
    timezone_city = CharField(null=True)
    title = CharField(null=True)
    tracker_sorting = IntegerField()
    uid = CharField(unique=True)
    units = IntegerField()
    week = CharField()

    class Meta:
        db_table = 'T_USER'


class DelegationLog(BaseModel):
    administrator = ForeignKeyField(db_column='administrator_id',
                                    rel_model=Administrator, to_field='id')
    id = BigIntegerField(primary_key=True)
    tid = ForeignKeyField(db_column='tid', rel_model=TerminalInfo,
                          to_field='tid')
    timestamp = BigIntegerField()
    uid = ForeignKeyField(db_column='uid', rel_model=User, to_field='uid')

    class Meta:
        db_table = 'T_DELEGATION_LOG'


class DevSupport(BaseModel):
    email = CharField()
    mobile = CharField()
    name = CharField()

    class Meta:
        db_table = 'T_DEV_SUPPORT'


class Download(BaseModel):
    category = CharField()
    count = BigIntegerField()
    id = BigIntegerField(primary_key=True)

    class Meta:
        db_table = 'T_DOWNLOAD'


class Ec(BaseModel):
    ec_name = CharField(null=True, unique=True)
    mobile = CharField(null=True)
    password = CharField(null=True)

    class Meta:
        db_table = 'T_EC'


class EcGroup(BaseModel):
    ec = ForeignKeyField(db_column='ec_id', null=True, rel_model=Ec,
                         to_field='id')
    name = CharField(null=True)

    class Meta:
        db_table = 'T_EC_GROUP'


class Email(BaseModel):
    content = TextField(null=True)
    email = CharField()
    from_addr = CharField(null=True)
    html = CharField()
    insert_time = CharField()
    send_status = IntegerField()
    subject = TextField(null=True)

    class Meta:
        db_table = 'T_EMAIL'


class EmailChangeLog(BaseModel):
    new_email = CharField()
    old_email = CharField(unique=True)

    class Meta:
        db_table = 'T_EMAIL_CHANGE_LOG'


class EmailOption(BaseModel):
    charge = IntegerField()
    heartbeat_lost = IntegerField()
    illegalmove = IntegerField()
    illegalshake = IntegerField()
    login = IntegerField()
    overspeed = IntegerField()
    powerfull = IntegerField()
    powerlow = IntegerField()
    region_enter = IntegerField()
    region_out = IntegerField()
    sos = IntegerField()
    stopping = IntegerField()
    uid = ForeignKeyField(db_column='uid', rel_model=User, to_field='uid',
                          unique=True)

    class Meta:
        db_table = 'T_EMAIL_OPTION'


class Event(BaseModel):
    category = IntegerField(null=True)
    eqp = IntegerField(db_column='eqp_id', null=True)
    event_time = IntegerField()
    fobid = CharField(null=True)
    lid = BigIntegerField(null=True)
    packet_time = BigIntegerField(null=True)
    pbat = CharField(null=True)
    pid = BigIntegerField()
    read_flag = IntegerField(null=True)
    rid = BigIntegerField(null=True)
    temp = FloatField(null=True)
    terminal_type = CharField(null=True)
    tid = CharField()

    class Meta:
        db_table = 'T_EVENT'
        indexes = (
            (('tid', 'packet_time'), False),
        )


class ExtEqp(BaseModel):
    id = BigIntegerField()
    con_mode = IntegerField()
    eqp_code = CharField()
    type = CharField()
    wire_color = CharField(null=True)

    class Meta:
        db_table = 'T_EXT_EQP'


class Feedback(BaseModel):
    category = CharField(null=True)
    contact = CharField(null=True)
    content = CharField(null=True)
    email = CharField(null=True)
    id = BigIntegerField(primary_key=True)
    isreplied = IntegerField()
    language = IntegerField()
    reply = CharField()
    reply_time = BigIntegerField()
    timestamp = BigIntegerField(null=True)

    class Meta:
        db_table = 'T_FEEDBACK'


class Fob(BaseModel):
    fobid = CharField(unique=True)
    tid = ForeignKeyField(db_column='tid', rel_model=TerminalInfo,
                          to_field='tid')

    class Meta:
        db_table = 'T_FOB'


class FusebillCountry(BaseModel):
    cid = CharField(null=True)
    iso = CharField(null=True)
    iso3 = CharField(null=True)
    name = CharField(null=True)

    class Meta:
        db_table = 'T_FUSEBILL_COUNTRY'


class FusebillProvince(BaseModel):
    cid = CharField(null=True)
    combinedisocode = CharField(db_column='combinedIsoCode', null=True)
    name = CharField(null=True)
    pid = CharField(null=True)
    subdivisionisocode = CharField(db_column='subdivisionIsoCode', null=True)

    class Meta:
        db_table = 'T_FUSEBILL_PROVINCE'


class Heartbeat(BaseModel):
    charging_status = IntegerField()
    gps = IntegerField()
    gsm = IntegerField()
    id = IntegerField()
    pbat = IntegerField()
    temp = IntegerField()
    tid = CharField()
    timestamp = IntegerField(index=True)

    class Meta:
        db_table = 'T_HEARTBEAT'
        indexes = (
            (('id', 'timestamp'), True),
            (('tid', 'timestamp'), False),
        )
        primary_key = CompositeKey('id', 'timestamp')


class HeartbeatBak(BaseModel):
    charging_status = IntegerField()
    gps = IntegerField()
    gsm = IntegerField()
    pbat = IntegerField()
    temp = IntegerField()
    tid = CharField()
    timestamp = IntegerField()

    class Meta:
        db_table = 'T_HEARTBEAT_bak'


class HlrCity(BaseModel):
    city = PrimaryKeyField(db_column='city_id')
    city_name = CharField()
    lat = BigIntegerField()
    lon = BigIntegerField()
    province = IntegerField(db_column='province_id')
    region_code = CharField()

    class Meta:
        db_table = 'T_HLR_CITY'


class HlrInfo(BaseModel):
    company = CharField(null=True)
    hlr_code = CharField(primary_key=True)
    prov_code = CharField()
    region_code = CharField()

    class Meta:
        db_table = 'T_HLR_INFO'


class HlrProvince(BaseModel):
    country = IntegerField(db_column='country_id', null=True)
    lat = BigIntegerField()
    ld_num = CharField(null=True)
    lon = BigIntegerField()
    province = PrimaryKeyField(db_column='province_id')
    province_name = CharField()

    class Meta:
        db_table = 'T_HLR_PROVINCE'


class InvoicenumSeq(BaseModel):
    class Meta:
        db_table = 'T_INVOICENUM_SEQ'


class Label(BaseModel):
    color = CharField(null=True)
    lid = CharField()
    name = CharField(null=True)
    uid = CharField(null=True)

    class Meta:
        db_table = 'T_LABEL'


class LabelTerminal(BaseModel):
    id = BigIntegerField(primary_key=True)
    lid = CharField()
    tid = CharField()

    class Meta:
        db_table = 'T_LABEL_TERMINAL'
        indexes = (
            (('lid', 'tid'), True),
        )


class Location(BaseModel):
    altitude = BigIntegerField()
    category = IntegerField()
    cellid = CharField(null=True)
    clatitude = BigIntegerField()
    clongitude = BigIntegerField()
    degree = DecimalField(null=True)
    ggp = CharField()
    gps = IntegerField(null=True)
    gsm = IntegerField(null=True)
    id = BigIntegerField()
    latitude = BigIntegerField()
    location_type = IntegerField()
    longitude = BigIntegerField()
    misc = CharField(null=True)
    name = TextField(null=True)
    name_en = TextField(null=True)
    pacc = FloatField(null=True)
    packet_time = BigIntegerField(null=True)
    pbat = IntegerField(null=True)
    recv_time = IntegerField()
    speed = IntegerField(null=True)
    status = IntegerField()
    temp = IntegerField()
    tid = CharField(index=True)
    timestamp = BigIntegerField(index=True)
    type = IntegerField()

    class Meta:
        db_table = 'T_LOCATION'
        indexes = (
            (('id', 'timestamp'), True),
            (('tid', 'timestamp'), False),
        )
        primary_key = CompositeKey('id', 'timestamp')


class LocationBak(BaseModel):
    altitude = BigIntegerField()
    category = IntegerField()
    cellid = CharField(null=True)
    clatitude = BigIntegerField()
    clongitude = BigIntegerField()
    degree = DecimalField(null=True)
    ggp = CharField()
    id = BigIntegerField(primary_key=True)
    latitude = BigIntegerField()
    location_type = IntegerField()
    longitude = BigIntegerField()
    misc = CharField(null=True)
    name = TextField(null=True)
    name_en = TextField(null=True)
    packet_time = BigIntegerField(null=True)
    speed = IntegerField(null=True)
    temp = IntegerField()
    tid = CharField(index=True)
    timestamp = BigIntegerField(index=True, null=True)
    type = IntegerField()

    class Meta:
        db_table = 'T_LOCATION_bak'
        indexes = (
            (('tid', 'timestamp'), False),
        )


class Maintain(BaseModel):
    choose_type = IntegerField()
    cumulative_mileage = FloatField(null=True)
    cumulative_time = BigIntegerField(null=True)
    init_maintain_mileage = FloatField(null=True)
    init_maintain_mileage_time = IntegerField(null=True)
    init_maintaintime = BigIntegerField(null=True)
    init_maintaintime_time = IntegerField(null=True)
    maintain_mileage = FloatField(null=True)
    maintain_mileage_time = IntegerField(null=True)
    maintaintime = BigIntegerField(null=True)
    maintaintime_time = IntegerField(null=True)
    reset_time = IntegerField(null=True)
    tid = CharField(null=True)

    class Meta:
        db_table = 'T_MAINTAIN'


class MaintainRecord(BaseModel):
    content = CharField(null=True)
    id = BigIntegerField(primary_key=True)
    insert_time = IntegerField(null=True)
    start_time = IntegerField(null=True)
    tid = CharField(null=True)

    class Meta:
        db_table = 'T_MAINTAIN_RECORD'


class MetaPrivilege(BaseModel):
    mnemonic = CharField(unique=True)
    name = CharField(unique=True)

    class Meta:
        db_table = 'T_META_PRIVILEGE'


class Permission(BaseModel):
    id = IntegerField()
    name = CharField(unique=True)

    class Meta:
        db_table = 'T_PERMISSION'


class PgVisitReport(BaseModel):
    geo_id = IntegerField(db_column='geo_id', null=True)
    poi_id = IntegerField(db_column='poi_id', null=True)
    tid = CharField(null=True)
    visit_time = IntegerField(null=True)
    departure_time = IntegerField(null=True)

    class Meta:
        db_table = 'T_PG_VISIT_REPORT'


class Poi(BaseModel):
    address = TextField()
    avatar = CharField()
    enter_alert = IntegerField()
    latitude = IntegerField()
    longitude = IntegerField()
    marker = CharField(null=True)
    name = CharField()
    out_alert = IntegerField()
    radius = FloatField()
    uid = ForeignKeyField(db_column='uid', rel_model=User, to_field='uid')

    class Meta:
        db_table = 'T_POI'


class PoiTerminal(BaseModel):
    pid = IntegerField()
    tid = CharField()

    class Meta:
        db_table = 'T_POI_TERMINAL'


class PoweroffTimeout(BaseModel):
    sms_flag = IntegerField(null=True)
    tid = ForeignKeyField(db_column='tid', rel_model=TerminalInfo,
                          to_field='tid', unique=True)
    timestamp = BigIntegerField(null=True)

    class Meta:
        db_table = 'T_POWEROFF_TIMEOUT'


class PrivilegeGroup(BaseModel):
    builtin = IntegerField()
    name = CharField(unique=True)

    class Meta:
        db_table = 'T_PRIVILEGE_GROUP'


class Privilege(BaseModel):
    administrator = ForeignKeyField(db_column='administrator_id',
                                    rel_model=Administrator, to_field='id')
    privilege_group = ForeignKeyField(db_column='privilege_group_id',
                                      rel_model=PrivilegeGroup, to_field='id')

    class Meta:
        db_table = 'T_PRIVILEGE'
        indexes = (
            (('administrator', 'privilege_group'), True),
        )
        primary_key = CompositeKey('administrator', 'privilege_group')


class PrivilegeGroupData(BaseModel):
    privilege_group = IntegerField(db_column='privilege_group_id', index=True)
    privilege = IntegerField(db_column='privilege_id', index=True)

    class Meta:
        db_table = 'T_PRIVILEGE_GROUP_DATA'
        indexes = (
            (('privilege_group', 'privilege'), True),
        )
        primary_key = CompositeKey('privilege', 'privilege_group')


class Province(BaseModel):
    cid = CharField(null=True)
    province = CharField(db_column='province_id', null=True)
    province_name = CharField(null=True)

    class Meta:
        db_table = 'T_PROVINCE'


class Region(BaseModel):
    cid = CharField(null=True)
    end_time = IntegerField()
    enter_alert = IntegerField()
    friday = CharField()
    hours = CharField()
    latitude = BigIntegerField(null=True)
    longitude = BigIntegerField(null=True)
    monday = CharField()
    name = CharField(null=True)
    out_alert = IntegerField()
    points = TextField(null=True)
    radius = FloatField(null=True)
    saturday = CharField()
    schedule = IntegerField()
    shape = IntegerField()
    start_time = IntegerField()
    sunday = CharField()
    thursday = CharField()
    tuesday = CharField()
    uid = ForeignKeyField(db_column='uid', null=True, rel_model=User,
                          to_field='uid')
    wednesday = CharField()

    class Meta:
        db_table = 'T_REGION'


class RegionTerminal(BaseModel):
    enter_alert = IntegerField()
    out_alert = IntegerField()
    rid = IntegerField(null=True)
    tid = CharField(null=True)

    class Meta:
        db_table = 'T_REGION_TERMINAL'


class Role(BaseModel):
    id = IntegerField()
    company_id = IntegerField()
    name = CharField()

    class Meta:
        db_table = 'T_ROLE'


class RolePermission(BaseModel):
    permission_id = IntegerField()
    role_id = IntegerField()

    class Meta:
        db_table = 'T_ROLE_PERMISSION'


class RuntimeStatus(BaseModel):
    defend_status = IntegerField(null=True)
    fob_pbat = IntegerField(null=True)
    gps = IntegerField(null=True)
    gsm = IntegerField(null=True)
    login = IntegerField(null=True)
    pbat = IntegerField(null=True)
    tid = CharField()
    timestamp = BigIntegerField(null=True)

    class Meta:
        db_table = 'T_RUNTIME_STATUS'


class Script(BaseModel):
    author = CharField(null=True)
    etag = CharField(null=True)
    filename = CharField(null=True)
    id = BigIntegerField(primary_key=True)
    last_modified = CharField(null=True)
    timestamp = BigIntegerField(null=True)
    version = CharField(null=True, unique=True)

    class Meta:
        db_table = 'T_SCRIPT'


class ScriptDownload(BaseModel):
    id = BigIntegerField(primary_key=True)
    reason = CharField(null=True)
    tid = CharField(null=True)
    timestamp = BigIntegerField()
    versionname = CharField(null=True)

    class Meta:
        db_table = 'T_SCRIPT_DOWNLOAD'


class Seq(BaseModel):
    class Meta:
        db_table = 'T_SEQ'


class Sms(BaseModel):
    category = IntegerField()
    content = TextField()
    fetch_time = BigIntegerField(null=True)
    iccid = CharField(null=True)
    id = BigIntegerField(primary_key=True)
    insert_time = BigIntegerField()
    mobile = CharField(null=True)
    msgid = IntegerField()
    operator = CharField(null=True)
    recv_status = IntegerField()
    retry_status = IntegerField()
    send_status = IntegerField()

    class Meta:
        db_table = 'T_SMS'


class SmsOption(BaseModel):
    charge = IntegerField()
    heartbeat_lost = IntegerField()
    illegalmove = IntegerField()
    illegalshake = IntegerField()
    login = IntegerField()
    overspeed = IntegerField()
    powerfull = IntegerField()
    powerlow = IntegerField()
    region_enter = IntegerField()
    region_out = IntegerField()
    sos = IntegerField()
    stopping = IntegerField()
    uid = ForeignKeyField(db_column='uid', rel_model=User, to_field='uid',
                          unique=True)

    class Meta:
        db_table = 'T_SMS_OPTION'


class Sos(BaseModel):
    email = CharField(null=True)
    id = BigIntegerField(primary_key=True)
    mobile = CharField()
    tid = ForeignKeyField(db_column='tid', rel_model=TerminalInfo,
                          to_field='tid', unique=True)

    class Meta:
        db_table = 'T_SOS'


class Sp(BaseModel):
    corp_name = CharField()
    email = CharField()
    id = BigIntegerField(primary_key=True)
    ip = CharField()
    mobile = CharField()
    name = CharField()
    password = CharField()
    sid = CharField()

    class Meta:
        db_table = 'T_SP'


class StatisticLog(BaseModel):
    agent = IntegerField()
    timestamp = IntegerField()
    tracker_add_daily = IntegerField()
    tracker_add_monthly = IntegerField()
    tracker_add_yearly = IntegerField()
    tracker_dea_daily = IntegerField()
    tracker_dea_monthly = IntegerField()
    tracker_dea_yearly = IntegerField()
    tracker_del_daily = IntegerField()
    tracker_del_monthly = IntegerField()
    tracker_del_yearly = IntegerField()
    tracker_offline = IntegerField()
    tracker_online = IntegerField()
    tracker_total = IntegerField()
    user_active = IntegerField()
    user_login_daily = IntegerField()
    user_login_monthly = IntegerField()
    user_login_yearly = IntegerField()
    user_sleepy = IntegerField()

    class Meta:
        db_table = 'T_STATISTIC_LOG'


class SubscriptionnumSeq(BaseModel):
    class Meta:
        db_table = 'T_SUBSCRIPTIONNUM_SEQ'


class TerminalInfoLog(BaseModel):
    add_time = IntegerField()
    agent = IntegerField()
    dea_time = IntegerField()
    del_time = IntegerField()
    last_time = IntegerField()
    op_type = IntegerField()
    tid = CharField()
    uid = CharField(null=True)

    class Meta:
        db_table = 'T_TERMINAL_INFO_LOG'


class TerminalLoginLog(BaseModel):
    reason = IntegerField()
    tid = CharField(index=True, null=True)
    timestamp = BigIntegerField(index=True)

    class Meta:
        db_table = 'T_TERMINAL_LOGIN_LOG'


class TerminalNotification(BaseModel):
    email = IntegerField(null=True)
    push = IntegerField(null=True)
    sms = IntegerField(null=True)
    tid = ForeignKeyField(db_column='tid', rel_model=TerminalInfo,
                          to_field='tid', unique=True)

    class Meta:
        db_table = 'T_TERMINAL_NOTIFICATION'


class TerminalOption(BaseModel):
    away = IntegerField(null=True)
    check_enable = IntegerField(null=True)
    heartbeat_lost = IntegerField(default=1)
    illegalmove = IntegerField(default=0)
    illegalshake = IntegerField(default=0)
    leave_destination = IntegerField(null=True)
    overspeed = IntegerField(default=0)
    poi = IntegerField(null=True)
    powerfull = IntegerField(default=0)
    powerlow = IntegerField(default=0)
    poweroff = IntegerField(null=True)
    region = IntegerField(default=0)
    sos = IntegerField(default=1)
    stopping = IntegerField(default=0)
    temperature = IntegerField(null=True)
    tid = ForeignKeyField(db_column='tid', rel_model=TerminalInfo,
                          to_field='tid', unique=True)
    usb_connect = IntegerField(null=True)
    usb_disconnect = IntegerField(null=True)

    class Meta:
        db_table = 'T_TERMINAL_OPTION'


class TerminalStatisticBaseInfo(BaseModel):
    avg_speed = FloatField(null=True)
    avg_temp = IntegerField(null=True)
    date_day = CharField(null=True)
    date_timestamp = BigIntegerField(null=True)
    distance = FloatField(null=True)
    drving_time = IntegerField(null=True)
    fuel = FloatField(null=True)
    gpio1 = CharField(null=True)
    gpio2 = CharField(null=True)
    gpio3 = CharField(null=True)
    id = BigIntegerField(primary_key=True)
    idle_periods = TextField(null=True)
    engine_time = IntegerField(null=True)
    idle_time = IntegerField(null=True)
    max_speed = FloatField(null=True)
    max_temp = IntegerField(null=True)
    min_temp = IntegerField(null=True)
    periods = TextField(null=True)
    speed_less_10 = IntegerField(null=True)
    speed_less_10_per = FloatField(null=True)
    speed_less_30 = IntegerField(null=True)
    speed_less_30_per = FloatField(null=True)
    speed_less_5 = IntegerField(null=True)
    speed_less_70 = IntegerField(null=True)
    speed_less_70_per = FloatField(null=True)
    speed_more_70 = IntegerField(null=True)
    speed_total_time = IntegerField(null=True)
    stops = IntegerField(null=True)
    stops_less_2hour = IntegerField(null=True)
    stops_less_30min = IntegerField(null=True)
    tid = CharField(null=True)

    class Meta:
        db_table = 'T_TERMINAL_STATISTIC_BASE_INFO'
        indexes = (
            (('tid', 'date_day'), True),
        )


class TerminalStatisticStateMileage(BaseModel):
    date_day = CharField(null=True)
    date_timestamp = BigIntegerField(null=True)
    distance = FloatField(null=True)
    id = BigIntegerField(primary_key=True)
    state = CharField(null=True)
    tid = CharField(null=True)

    class Meta:
        db_table = 'T_TERMINAL_STATISTIC_STATE_MILEAGE'
        indexes = (
            (('tid', 'date_day', 'state'), True),
        )


class TidEmailOption(BaseModel):
    charge = IntegerField()
    heartbeat_lost = IntegerField()
    illegalmove = IntegerField()
    illegalshake = IntegerField()
    login = IntegerField()
    overspeed = IntegerField()
    powerfull = IntegerField()
    powerlow = IntegerField()
    region_enter = IntegerField()
    region_out = IntegerField()
    sos = IntegerField()
    stopping = IntegerField()
    tid = ForeignKeyField(db_column='tid', rel_model=TerminalInfo,
                          to_field='tid', unique=True)

    class Meta:
        db_table = 'T_TID_EMAIL_OPTION'


class TidSmsOption(BaseModel):
    charge = IntegerField()
    heartbeat_lost = IntegerField()
    illegalmove = IntegerField()
    illegalshake = IntegerField()
    login = IntegerField()
    overspeed = IntegerField()
    powerfull = IntegerField()
    powerlow = IntegerField()
    region_enter = IntegerField()
    region_out = IntegerField()
    sos = IntegerField()
    stopping = IntegerField()
    tid = ForeignKeyField(db_column='tid', rel_model=TerminalInfo,
                          to_field='tid', unique=True)

    class Meta:
        db_table = 'T_TID_SMS_OPTION'


class TimeZone(BaseModel):
    id = IntegerField()
    utcoffset = CharField()
    zone_name = CharField(unique=True)

    class Meta:
        db_table = 'T_TIME_ZONE'
        indexes = (
            (('id', 'zone_name'), True),
        )
        primary_key = CompositeKey('id', 'zone_name')


class Total(BaseModel):
    choose_type = IntegerField()
    id = BigIntegerField(primary_key=True)
    init_drivingtime = BigIntegerField(null=True)
    init_drivingtime_time = BigIntegerField(null=True)
    init_mileage = IntegerField(null=True)
    init_mileage_time = BigIntegerField(null=True)
    tid = CharField(null=True)
    total_drivingtime = BigIntegerField(null=True)
    total_drivingtime_time = BigIntegerField(null=True)
    total_mileage = FloatField(null=True)
    total_mileage_time = BigIntegerField(null=True)

    class Meta:
        db_table = 'T_TOTAL'


class TrackerAssignment(BaseModel):
    tid = CharField()
    uid = CharField()

    class Meta:
        db_table = 'T_TRACKER_ASSIGNMENT'
        indexes = (
            (('uid', 'tid'), True),
        )


class TrackerBindingLog(BaseModel):
    iccid = CharField()
    sn = CharField()
    timestamp = IntegerField()

    class Meta:
        db_table = 'T_TRACKER_BINDING_LOG'


class TrackerUserBindingLog(BaseModel):
    agent_id = IntegerField(db_column='agent_id')
    iccid = CharField()
    oper_type = IntegerField()
    sn = CharField()
    timestamp = IntegerField()
    uid = CharField()

    class Meta:
        db_table = 'T_TRACKER_USER_BINDING_LOG'


class TracOrdernumSeq(BaseModel):
    class Meta:
        db_table = 'T_TRAC_ORDERNUM_SEQ'


class UidVid(BaseModel):
    id = BigIntegerField(primary_key=True)
    uid = CharField()
    vid = CharField()

    class Meta:
        db_table = 'T_UID_VID'
        indexes = (
            (('vid', 'uid'), True),
        )


class UserLoginLog(BaseModel):
    agent = IntegerField(db_column='agent_id')
    client = CharField(null=True)
    method = CharField(null=True)
    timestamp = IntegerField()
    uid = CharField(null=True)
    versionname = CharField(null=True)

    class Meta:
        db_table = 'T_USER_LOGIN_LOG'


class VidTid(BaseModel):
    id = BigIntegerField(primary_key=True)
    tid = CharField()
    vid = CharField()

    class Meta:
        db_table = 'T_VID_TID'
        indexes = (
            (('vid', 'tid'), True),
        )


class ViewerOption(BaseModel):
    history = IntegerField()
    is_permit = IntegerField(null=True)
    locate = IntegerField()
    opt = CharField(db_column='opt_id')
    opt_user = CharField()
    reports = IntegerField()
    tid = CharField()
    track = IntegerField()
    tracklq = IntegerField()
    vid = ForeignKeyField(db_column='vid', rel_model=User, to_field='uid')
    week = CharField()

    class Meta:
        db_table = 'T_VIEWER_OPTION'
        indexes = (
            (('tid', 'vid'), True),
        )


class VEvent(BaseModel):
    altitude = BigIntegerField()
    category = IntegerField()
    clatitude = BigIntegerField()
    clongitude = BigIntegerField()
    degree = DecimalField(null=True)
    eid = IntegerField()
    event_time = IntegerField()
    fobid = CharField(null=True)
    latitude = BigIntegerField()
    location_type = IntegerField()
    longitude = BigIntegerField()
    misc = CharField(null=True)
    name = TextField(null=True)
    name_en = TextField(null=True)
    pacc = FloatField(null=True)
    pbat = CharField(null=True)
    pid = BigIntegerField()
    read_flag = IntegerField(null=True)
    rid = BigIntegerField(null=True)
    speed = IntegerField(null=True)
    terminal_type = CharField(null=True)
    tid = CharField()
    timestamp = BigIntegerField()
    type = IntegerField()

    class Meta:
        db_table = 'V_EVENT'
