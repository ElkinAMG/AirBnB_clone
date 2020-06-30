#!/usr/bin/python3
"""
The console
"""
from models.base_model import BaseModel
from models.user import User
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.amenity import Amenity
from models import storage
import cmd
import shlex


class HBNBCommand(cmd.Cmd):
    """
    Some description
    """

    class_list = [
        "BaseModel", "User", "Place", "State", "City", "Amenity", "Review"
    ]
    prompt = "(hbnb) "
    cl_n_m = "** class name missing **"
    cl_d_e = "** class doesn't exist **"
    in_i_m = "** instance id missing **"
    id_d_e = "** no instance found **"
    att_mis = "** attribute name missing **"
    v_miss = "** value missing **"

    @staticmethod
    def perror(t_error="", str="", error="", cls_name=""):
        """Prints a error message.
        """

        r_val = True

        if t_error == "missing":
            if len(str) == 0:
                print(error)
                r_val = False
        elif t_error == "exist'nt":
            if str not in HBNBCommand.class_list:
                print(error)
                r_val = False
        elif t_error == "id_exist":
            found = False
            for k, v in storage.all().items():
                if k == "{}.{}".format(cls_name, str):
                    found = True
                    break
            if not found:
                print(error)
                r_val = False

        return (r_val)

    def do_create(self, class_name=""):
        """Creates a new instance of the cass BaseModel
        """

        class_name = class_name.split(" ")[0]

        if self.perror("missing", class_name, self.cl_n_m):
            if self.perror("exist'nt", class_name, self.cl_d_e):
                self.ins = eval("{}()".format(class_name))
                self.ins.save()
                print(self.ins.id)

    def do_show(self, inst=""):
        """Shows a description of an instance.
        """

        c_i = ["", ""]

        c_i[0] = inst.split(" ")[0]
        try:
            c_i[1] = inst.split(" ")[1]
        except:
            c_i[1] = ""

        if self.perror("missing", c_i[0], self.cl_n_m):
            if self.perror("exist'nt", c_i[0], self.cl_d_e):
                if self.perror("missing", c_i[1], self.in_i_m):
                    if self.perror("id_exist", c_i[1], self.id_d_e, c_i[0]):
                        for k, v in storage.all().items():
                            if k == "{}.{}".format(c_i[0], c_i[1]):
                                print(v)
                                break

    def do_destroy(self, arguments=""):
        """Destorys or deletes an object from file
        """
        args = ["", ""]

        args[0] = arguments.split(" ")[0]

        try:
            args[1] = arguments.split(" ")[1]
        except:
            args[1] = ""

        if self.perror("missing", args[0], self.cl_n_m):
            if self.perror("exist'nt", args[0], self.cl_d_e):
                if self.perror("missing", args[1], self.in_i_m):
                    objects = storage.all()
                    obj = "{}.{}".format(args[0], args[1])
                    if obj in objects:
                        del objects[obj]
                        storage.save()
                    else:
                        print("** no instance found **")

    def do_all(self, arguments=""):
        """prints the string description of objects
        """

        objects = storage.all()
        objs_str = []

        if len(arguments) == 0:
            for k, v in objects.items():
                objs_str.append(v.__str__())
        else:
            if arguments in self.class_list:
                for k, v in objects.items():
                    if arguments == k.split(".")[0]:
                        objs_str.append(v.__str__())
            else:
                print(self.cl_d_e)
                return
        print(objs_str)

    def do_update(self, args):
        """Some description
        """
        ci = ["", "", "", ""]

        args = shlex.split(args)

        for i in range(4):
            try:
                ci[i] = args[i]
            except:
                ci[i] = ""

        if self.perror("missing", ci[0], self.cl_n_m):
            if self.perror("exist'nt", ci[0], self.cl_d_e):
                if self.perror("missing", ci[1], self.in_i_m):
                    if self.perror("id_exist", ci[1], self.id_d_e, ci[0]):
                        if self.perror("missing", ci[2], self.att_mis):
                            if self.perror("missing", ci[3], self.v_miss):
                                atts = ["id", "created_at", "updated_at"]
                                for k, v in storage.all().items():
                                    if k == "{}.{}".format(ci[0], ci[1]):
                                        if ci[2] not in atts:
                                            try:
                                                setattr(
                                                    v, ci[2], eval(ci[3]))
                                            except:
                                                setattr(
                                                    v, ci[2], ci[3])
                                                storage.save()

    def do_quit(self, *args):
        """Exits the console when command 'quit' is entered
        """

        return True

    def do_EOF(self, *args):
        """Exits the program when end of file or 'EOF' is encountered
        """

        return True

    def emptyline(self):
        if self.lastcmd:
            self.lastcmd = ""
            return self.onecmd('\n')


if __name__ == '__main__':
    HBNBCommand().cmdloop(
        "==============================\
        \n    Welcome To HBTN-BnB\n==============================\n")
