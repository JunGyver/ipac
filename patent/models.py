from django.db import models

class Master(models.Model):
    data_id = models.AutoField(primary_key=True)
    nation = models.TextField(blank=True, null=True)
    db_gubun = models.TextField(blank=True, null=True)
    p_u = models.TextField(blank=True, null=True)
    doc_type = models.TextField(blank=True, null=True)
    title = models.TextField(blank=True, null=True)
    title2 = models.TextField(blank=True, null=True)
    abstract = models.TextField(blank=True, null=True)
    abstract2 = models.TextField(blank=True, null=True)
    claim = models.TextField(blank=True, null=True)
    claim2 = models.TextField(blank=True, null=True)
    claim_cnt = models.TextField(blank=True, null=True)
    memo = models.TextField(blank=True, null=True)
    file_num = models.TextField(blank=True, null=True)
    file_date = models.TextField(blank=True, null=True)
    trans_date = models.TextField(blank=True, null=True)
    pub_num = models.TextField(blank=True, null=True)
    pub_date = models.TextField(blank=True, null=True)
    pub_num2 = models.TextField(blank=True, null=True)
    pub_date2 = models.TextField(blank=True, null=True)
    reg_num = models.TextField(blank=True, null=True)
    reg_date = models.TextField(blank=True, null=True)
    pub_num3 = models.TextField(blank=True, null=True)
    applicant = models.TextField(blank=True, null=True)
    applicant2 = models.TextField(blank=True, null=True)
    applicant_nation = models.TextField(blank=True, null=True)
    applicant_cnt = models.TextField(blank=True, null=True)
    applicant_code = models.TextField(blank=True, null=True)
    applicant_eng = models.TextField(blank=True, null=True)
    applicant_kr = models.TextField(blank=True, null=True)
    applicant_org = models.TextField(blank=True, null=True)
    applicant_sign = models.TextField(blank=True, null=True)
    inventor = models.TextField(blank=True, null=True)
    inventor2 = models.TextField(blank=True, null=True)
    inventor_nation = models.TextField(blank=True, null=True)
    inventor_cnt = models.TextField(blank=True, null=True)
    agent = models.TextField(blank=True, null=True)
    priority_num = models.TextField(blank=True, null=True)
    priority_nation = models.TextField(blank=True, null=True)
    priority_date = models.TextField(blank=True, null=True)
    first_priority_num = models.TextField(blank=True, null=True)
    first_priority_nation = models.TextField(blank=True, null=True)
    first_priority_date = models.TextField(blank=True, null=True)
    pct_num = models.TextField(blank=True, null=True)
    pct_date = models.TextField(blank=True, null=True)
    pct_pub_num = models.TextField(blank=True, null=True)
    pct_pub_date = models.TextField(blank=True, null=True)
    pct_nation = models.TextField(blank=True, null=True)
    epc_nation = models.TextField(blank=True, null=True)
    org_cpc_main = models.TextField(blank=True, null=True)
    org_cpc_all = models.TextField(blank=True, null=True)
    org_ipc_main = models.TextField(blank=True, null=True)
    org_ipc_all = models.TextField(blank=True, null=True)
    org_usclass_main = models.TextField(blank=True, null=True)
    org_usclass_all = models.TextField(blank=True, null=True)
    org_fi = models.TextField(blank=True, null=True)
    org_fterm = models.TextField(blank=True, null=True)
    org_theme_code = models.TextField(blank=True, null=True)
    cur_cpc_main = models.TextField(blank=True, null=True)
    cur_cpc_all = models.TextField(blank=True, null=True)
    cur_ipc_main = models.TextField(blank=True, null=True)
    cur_ipc_all = models.TextField(blank=True, null=True)
    cur_usclass_main = models.TextField(blank=True, null=True)
    cur_usclass_all = models.TextField(blank=True, null=True)
    cur_fi = models.TextField(blank=True, null=True)
    cur_fterm = models.TextField(blank=True, null=True)
    b_cnt = models.TextField(blank=True, null=True)
    b_and_cited = models.TextField(blank=True, null=True)
    b_cited = models.TextField(blank=True, null=True)
    np_cited = models.TextField(blank=True, null=True)
    f_cnt = models.TextField(blank=True, null=True)
    f_and_cited = models.TextField(blank=True, null=True)
    f_cited = models.TextField(blank=True, null=True)
    epo_family = models.TextField(blank=True, null=True)
    epo_family_cnt = models.TextField(blank=True, null=True)
    family_basic_num = models.TextField(blank=True, null=True)
    family_num = models.TextField(blank=True, null=True)
    family_cnt = models.TextField(blank=True, null=True)
    family_file_cnt = models.TextField(blank=True, null=True)
    family_nation_cnt = models.TextField(blank=True, null=True)
    status_krjp = models.TextField(blank=True, null=True)
    status_us = models.TextField(blank=True, null=True)
    exam_req = models.TextField(blank=True, null=True)
    expire_date = models.TextField(blank=True, null=True)
    patentee = models.TextField(blank=True, null=True)
    patentee2 = models.TextField(blank=True, null=True)
    patentee_code = models.TextField(blank=True, null=True)
    patentee_eng = models.TextField(blank=True, null=True)
    patentee_kr = models.TextField(blank=True, null=True)
    docdb_status = models.TextField(blank=True, null=True)
    org_link = models.TextField(blank=True, null=True)
    trans_link = models.TextField(blank=True, null=True)
    detail_link = models.TextField(blank=True, null=True)
    detail_link_login = models.TextField(blank=True, null=True)
    re_fig = models.TextField(blank=True, null=True)
    fig_cnt = models.TextField(blank=True, null=True)
    in_out = models.TextField(blank=True, null=True)
    correction = models.TextField(blank=True, null=True)
    wipsonkey = models.TextField(blank=True, null=True)
    tags = models.TextField(blank=True, null=True)
    claim_grade = models.TextField(blank=True, null=True)
    gijun_num = models.TextField(blank=True, null=True)
    gijun_date = models.TextField(blank=True, null=True)
    img_src = models.TextField(blank=True, null=True)
    major = models.TextField(blank=True, null=True)
    main_inventor = models.TextField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'st_master'

    def get_applicant(self):
        return self.applicant.split('|')

    def get_inventor(self):
        return self.inventor.split('|')

    def get_patentee(self):
        return self.patentee.split('|')

    def get_tags(self):
        return StTag.objects.filter(tag_code__in=[x.strip() for x in self.tags.split('|')])

    def get_application_num(self):
        return self.file_num.replace('-', '')

    def get_main_image_url(self):
        return self.main_image.get_url()

    def store(self):
        self.save()
        return self

    def get_b_references(self):
        return StReference.objects.filter(ref_num__in=[x.strip().replace('(BE)', '').replace('(FE)', '') for x in self.b_and_cited.split('|')])

    def get_f_references(self):
        return StReference.objects.filter(ref_num__in=[x.strip().replace('(BE)', '').replace('(FE)', '') for x in self.f_and_cited.split('|')])

class History(models.Model):
    applicationNumber  = models.CharField(max_length=200, null=True)
    documentNumber     = models.CharField(max_length=200, null=True)
    documentDate       = models.CharField(max_length=200, null=True)
    documentTitle      = models.CharField(max_length=200, null=True)
    documentTitleEng   = models.CharField(max_length=200, null=True)
    status             = models.CharField(max_length=200, null=True)
    statusEng          = models.CharField(max_length=200, null=True)
    step               = models.CharField(max_length=200, null=True)
    trialNumber        = models.CharField(max_length=200, null=True)
    registrationNumber = models.CharField(max_length=200, null=True)
    master             = models.ForeignKey('Master', on_delete=models.SET_NULL, null=True)

    class Meta:
        db_table = 'histories'
