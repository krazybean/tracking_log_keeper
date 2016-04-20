from MySQLdb import escape_string

list_subsystems = """
    SELECT id, name, updated
    FROM subsystems;
"""

new_subsystem = """
    INSERT INTO subsystems
    (id, name)
    VALUES
    (%s, %s);
"""

create_template = """
    CREATE TABLE %s (
    id int NOT NULL,
    """


def bad_word(value):
    """ checking contents """
    func_ops = ['insert', 'delete', 'drop', 'update',
                'null', 'select', 'union', 'truncate']
    if value.lower() in func_ops:
        return False
    return True


def create_template(name, fields):
    """ Creates dynamic template """
    types = ['varchar', 'int']
    create = ['CREATE TABLE {0} ( id int NOT NULL'.format(escape_string(name))]
    for fname, ftype in fields.items():
        if not bad_word(fname) or not bad_word(ftype):
            msg = 'Reserved keyword identified at {0}/{1}'
            return {'error': msg.format(fname, ftype)}
        if ftype not in types:
            msg = 'Invalid type: {0}, valid: {1}'
            return {'error': msg.format(ftype, types)}
        create.append('{0} {1} NOT NULL'.format(escape_string(fname),
                                                escape_string(ftype)))
    create.append('PRIMARY KEY (id));')
    return ',\n'.join(create)


def select_template(name, fields):
    """ Select dynamic from template """
    select = ["SELECT id"]
    for fname, _ in fields.items():
        select.append('{0}'.format(escape_string(fname)))
    select.append('FROM {0} LIMIT 10;'.format(escape_string(name)))
    return ', '.join(select)


def insert_template(name, fields, data):
    """ Inserts into template """
    insert = ['INSERT INTO {0} ('.format(name)]
    flist = []
    for fname, _ in fields.items():
        if not bad_word(fname):
            msg = 'Reserved keyword identified at {0}/{1}'
            return {'error': msg.format(fname, ftype)}
        flist.append(fname)
    insert.append(', '.join(flist))
    insert.append(') VALUES (')
    dlist = []
    for _, dvalue in data.items():
        if not bad_word(dvalue):
            msg = 'Reserved keyword identified at {0}/{1}'
            return {'error': msg.format(fname, ftype)}
        dlist.append(dvalue)
    insert.append(', '.join(dlist))
    insert.append(');')
    return ' '.join(insert)


if __name__ == '__main__':
    name = 'test'
    fields = {'testfield1': 'varchar',
              'testfield2': 'int',
              'testfield3': 'varchar'}

    data = {'testfield1': 'test_data1',
            'testfield2': 'test_data2',
            'testfield3': 'test_data3'}

    print create_template(name, fields)
    print select_template(name, fields)
    print insert_template(name, fields, data)
