# -*- utf-8 -*-
import os

# file_p = str(os.path.join(os.path.expanduser("~"), 'Desktop')) + "//1"
spf = str(os.path.join(os.path.expanduser("~"), 'Desktop'))
file_p = ''
xml_path = ''

count = None


class uc:
    def read(self):
        file_path = str(file_p) + "//UC_A01_01Context.xml"
        rs = open(file_path, "r+")
        result = rs.readlines()
        rs.close()
        return result

    def add(self):
        result = self.read()
        rr = result

        for flag in range(1, int(count) + 1):
            file_name = xml_path + str(flag)
            import os
            if os.path.exists(xml_path) is False:
                os.mkdir(xml_path)
            if os.path.exists(file_name) is False:
                os.mkdir(file_name)
            xml_write = open(str(file_name) + "\\UC_A01_01Context.xml", "w+")
            print(str(flag) + ".......")
            for index in range(len(rr)):
                if flag < 10:
                    sflag = str(flag).zfill(2)
                else:
                    sflag = str(flag)
                if "/UC_A01_01/RP_A01_01_01" in rr[index]:
                    tmp = "/UC_A" + sflag + "_01/RP_A01_" + sflag + "_01"
                    print(tmp)
                    rr[index] = str(rr[index]).replace("/UC_A01_01/RP_A01_01_01", tmp)

                if "/UC_A01_01/SC_A01_01" in rr[index]:
                    tmp = "/UC_A" + sflag + "_01/SC_A01_" + sflag
                    rr[index] = str(rr[index]).replace("/UC_A01_01/SC_A01_01", tmp)

                xml_write.write(rr[index])
            xml_write.close()
            rr = self.read()


class blog:
    def read_blog(self):
        file_path = str(file_p) + "//blogic-UC_A01_01-io.xml"
        rs = open(file_path, "r+")
        result = rs.readlines()
        rs.close()
        return result

    def add_blog(self):
        result = self.read_blog()
        rr = result

        for flag in range(1, int(count) + 1):
            file_name = xml_path + str(flag)
            import os
            if os.path.exists(xml_path) is False:
                os.mkdir(xml_path)
            if os.path.exists(file_name) is False:
                os.mkdir(file_name)
            xml_write = open(str(file_name) + "\\blogic-UC_A01_01-io.xml", "w+")
            print(str(flag) + ".......")
            for index in range(len(rr)):
                if flag < 10:
                    sflag = str(flag).zfill(2)
                else:
                    sflag = str(flag)
                if "/RP_A01_01_01" in rr[index]:
                    tmp = "/RP_A01_" + sflag + "_01"
                    print(tmp)
                    rr[index] = str(rr[index]).replace("/RP_A01_01_01", tmp)

                xml_write.write(rr[index])
            xml_write.close()
            rr = self.read_blog()


class struts:
    def read_struts(self):
        file_path = str(file_p) + "//struts-UC_A01_01-config.xml"
        rs = open(file_path, "r+")
        result = rs.readlines()
        rs.close()
        return result

    def add_struts(self):
        result = self.read_struts()
        rr = result

        for flag in range(1, int(count) + 1):
            file_name = xml_path + str(flag)
            import os
            if os.path.exists(xml_path) is False:
                os.mkdir(xml_path)
            if os.path.exists(file_name) is False:
                os.mkdir(file_name)
            xml_write = open(str(file_name) + "\\struts-UC_A01_01-config.xml", "w+")
            print(str(flag) + ".......")
            for index in range(len(rr)):
                if flag < 10:
                    sflag = str(flag).zfill(2)
                else:
                    sflag = str(flag)

                if "action" in str(rr[index]):
                    if "path" in str(rr[index]):
                        if "_A01_01" in rr[index]:
                            tmp = "_A01_" + sflag
                            print(tmp)
                            rr[index] = str(rr[index]).replace("_A01_01", tmp)

                xml_write.write(rr[index])
            xml_write.close()
            rr = self.read_struts()


def man():
    import threading
    t1 = threading.Thread(target=uc().add)
    t2 = threading.Thread(target=blog().add_blog)
    t3 = threading.Thread(target=struts().add_struts)
    t1.start()
    import time
    time.sleep(1)
    t2.start()
    time.sleep(1)
    t3.start()
    t1.join()
    t2.join()
    t3.join()
