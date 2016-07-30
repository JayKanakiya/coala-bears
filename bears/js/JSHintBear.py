import json

from coalib.bearlib.abstractions.Linter import linter
from coalib.bears.requirements.NpmRequirement import NpmRequirement


def bool_or_str(value):
    try:
        return bool(value)
    except:
        return str(value)


def bool_or_int(value):
    try:
        return bool(value)
    except:
        return int(value)


@linter(executable='jshint',
        output_format='regex',
        output_regex=r'.+?: line (?P<line>\d+), col (?P<column>\d+), '
                     r'(?P<message>.+) \((?P<severity>[EWI])\d+\)')
class JSHintBear:
    """
    Detect errors and potential problems in JavaScript code and to enforce
    appropriate coding conventions. For example, problems like syntax errors,
    bugs due to implicit type conversion, leaking variables and much more
    can be detected.

    For more information on the analysis visit <http://jshint.com/>
    """

    LANGUAGES = {"JavaScript"}
    REQUIREMENTS = {NpmRequirement('jshint', '2')}
    AUTHORS = {'The coala developers'}
    AUTHORS_EMAILS = {'coala-devel@googlegroups.com'}
    LICENSE = 'AGPL-3.0'
    CAN_DETECT = {'Formatting', 'Syntax', 'Complexity', 'Unused Code'}

    @staticmethod
    def generate_config(filename, file,
                        allow_bitwise_operators: bool=False,
                        allow_prototype_overwrite: bool=False,
                        force_braces: bool=True,
                        allow_type_coercion: bool=False,
                        allow_future_identifiers: bool=True,
                        allow_typeof: bool=True,
                        force_filter_forin: bool=True,
                        allow_funcscope: bool=False,
                        iterator: bool=False,
                        prohibit_arg: bool=True,
                        allow_comma_operator: bool=True,
                        allow_non_breaking_whitespace: bool=False,
                        prohibit_new: bool=False,
                        prohibit_undefined: bool=True,
                        prohibit_groups: bool=False,
                        prohibit_variable_statements: bool=False,
                        allow_missing_semicolon: bool=False,
                        allow_debugger: bool=False,
                        allow_assignment_comparisions: bool=False,
                        allow_eval: bool=False,
                        allow_global_strict: bool=False,
                        allow_increment: bool=False,
                        allow_proto: bool=False,
                        allow_scripturls: bool=False,
                        allow_singleton: bool=False,
                        allow_this_statements: bool=False,
                        allow_with_statements: bool=False,
                        using_mozilla: bool=False,
                        allow_noyield: bool=False,
                        allow_eqnull: bool=False,
                        allow_last_semicolon: bool=False,
                        allow_func_in_loop: bool=False,
                        allow_expr_in_assignments: bool=False,
                        use_es6_syntax: bool=False,
                        use_es3_array: bool=False,
                        environment_mootools: bool=False,
                        environment_couch: bool=False,
                        environment_jasmine: bool=False,
                        environment_jquery: bool=False,
                        environment_node: bool=False,
                        environment_qunit: bool=False,
                        environment_rhino: bool=False,
                        environment_shelljs: bool=False,
                        environment_prototypejs: bool=False,
                        environment_yui: bool=False,
                        environment_mocha: bool=True,
                        environment_module: bool=False,
                        environment_wsh: bool=False,
                        environment_worker: bool=False,
                        environment_nonstandard: bool=False,
                        environment_browser: bool=True,
                        environment_browserify: bool=False,
                        environment_devel: bool=True,
                        environment_dojo: bool=False,
                        environment_typed: bool=False,
                        environment_phantom: bool=False,
                        max_statements: bool_or_int=False,
                        max_depth: bool_or_int=False,
                        max_parameters: bool_or_int=False,
                        cyclomatic_complexity: bool_or_int=False,
                        shadow: bool_or_str=False,
                        allow_unused_variables: bool_or_str=False,
                        allow_latedef: bool_or_str=False,
                        es_version: int=5,
                        jshint_config: str=""):
        """
        :param allow_bitwise_operators:
            Prohibits the use of bitwise operators when its value is ``False``.
        :param allow_prototype_overwrite:
            This options allows overwriting prototypes of native objects such as
            ``Array``.
        :param force_braces:
            This option requires you to always put curly braces around blocks
            in loops and conditionals.
        :param allow_type_coercion:
            This options allows the use of ``==`` and ``!=``.
        :param allow_future_identifiers:
            This option allows the use of identifiers which are defined in
            future versions of JavaScript.
        :param allow_typeof:
            This option enables warnings about invalid ``typeof`` operator
            values.
        :param force_filter_forin:
            This option requires all ``for in`` loops to filter object's items.
        :param iterator:
            This option suppresses warnings about the ``__iterator__``
            property.
        :param allow_funcscope:
            This option suppresses warnings about declaring variables inside of
            control structures while accessing them later from outside.
        :param prohibit_arg:
            This option prohibits the use of ``arguments.caller`` and
            ``arguments.callee``.
        :param allow_comma_operator:
            This option allows the use of the comma operator.
        :param allow_non_breaking_whitespace:
            Allows "non-breaking whitespace characters".
        :param prohibit_new:
            This option prohibits the use of constructor functions for
            side-effects.
        :param prohibit_undefined:
            This option prohibits the use of explicitly undeclared variables.
        :param prohibit_groups:
            This option prohibits the use of the grouping operator when it is
            not strictly required.
        :param prohibit_variable_statements:
            This option forbids the use of VariableStatements.
        :param allow_missing_semicolon:
            This option suppresses warnings about missing semicolons.
        :param allow_debugger:
            This option suppresses warnings about the ``debugger`` statements.
        :param allow_assignment_comparisions:
            This option suppresses warnings about the use of assignments in
            cases where comparisons are expected.
        :param allow_eval:
            This options suppresses warnings about the use of ``eval``
            function.
        :param allow_global_strict:
            This option suppresses warnings about the use of global strict
            mode.
        :param allow_increment:
            This option suppresses warnings about the use of unary increment
            and decrement operators.
        :param allow_proto:
            This option suppresses warnings about the ``__proto__`` property.
        :param allow_scripturls:
            This option suppresses warnings about the use of script-targeted
            URLs.
        :param allow_singleton:
            This option suppresses warnings about constructions like
            ``new function () { ... }`` and ``new Object;`` sometimes used to
            produce singletons.
        :param allow_this_statements:
            This option suppresses warnings about possible strict violations
            when the code is running in strict mode and ``this`` is used in a
            non-constructor function.
        :param allow_with_statements:
            This option suppresses warnings about the use of the ``with``
            statement.
        :param using_mozilla:
            This options tells JSHint that your code uses Mozilla JavaScript
            extensions.
        :param allow_noyield:
            This option suppresses warnings about generator functions with no
            ``yield`` statement in them.
        :param allow_eqnull:
            This option suppresses warnings about ``== null`` comparisons.
        :param allow_last_semicolon:
            This option suppresses warnings about missing semicolons for the
            last statement.
        :param allow_func_in_loop:
            This option suppresses warnings about functions inside of loops.
        :param allow_expr_in_assignments:
            This option suppresses warnings about the use of expressions where
            normally assignments or function calls are expected.
        :param use_es3_array:
            This option tells JSHintBear ES3 array elision elements, or empty
            elements are used.
        :param use_es3_array:
            This option tells JSHint ECMAScript 6 specific syntax is used.
        :param environment_mootools:
            This option defines globals exposed by the Mootools.
        :param environment_couch:
            This option defines globals exposed by CouchDB.
        :param environment_jasmine:
            This option defines globals exposed by Jasmine.
        :param environment_jquery:
            This option defines globals exposed by Jquery.
        :param environment_node:
            This option defines globals exposed by Node.
        :param environment_qunit:
            This option defines globals exposed by Qunit.
        :param environment_rhino:
            This option defines globals exposed when the code is running inside
            rhino runtime environment.
        :param environment_shelljs:
            This option defines globals exposed by the ShellJS.
        :param environment_prototypejs:
            This option defines globals exposed by the Prototype.
        :param environment_yui:
            This option defines globals exposed by the YUI JavaScript
            Framework.
        :param environment_mocha:
            This option defines globals exposed by the "BDD" and "TDD" UIs of
            the Mocha unit testing framework.
        :param environment_module:
            This option informs JSHintBear that the input code describes an
            ECMAScript 6 module.
        :param environment_wsh:
            This option defines globals available when the code is running as a
            script for the Windows Script Host.
        :param environment_worker:
            This option defines globals available when the code is running
            inside of a Web Worker.
        :param environment_nonstandard:
            This option defines non- standard but widely adopted globals such
            as ``escape`` and ``unescape``.
        :param environment_browser:
            This option defines globals exposed by modern browsers.
        :param environment_browserify:
            This option defines globals available when using the Browserify.
        :param environment_devel:
            This option defines globals that are usually used for debugging:
            ``console``, ``alert``, etc.
        :param environment_dojo:
            This option defines globals exposed by the Dojo Toolkit.
        :param environment_typed:
            This option defines globals for typed array constructors.
        :param environment_phantom:
            This option defines globals available when your core is running
            inside of the PhantomJS runtime environment.
        :param max_statements:
            Maximum number of statements allowed per function.
        :param max_depth:
            This option lets you control how nested do you want your blocks to
            be.
        :param max_parameters:
            Maximum number of parameters allowed per function.
        :param cyclomatic_complexity:
            Maximum cyclomatic complexity in the code.
        :param shadow:
            This option suppresses warnings about variable shadowing i.e.
            declaring a variable that had been already declared somewhere in
            the outer scope.

            - "inner" - check for variables defined in the same scope only
            - "outer" - check for variables defined in outer scopes as well
            - False - same as inner
            - True  - allow variable shadowing
        :param allow_unused_variables:
            Allows when variables are defined but never used. This can be set
            to ""vars"" to only check for variables, not function parameters, or
            ""strict"" to check all variables and parameters.
        :param allow_latedef:
            This option prohibits the use of a variable before it was defined.
            Setting this option to "nofunc" will allow function declarations to
            be ignored.
        :param es_version:
            This option is used to specify the ECMAScript version to which the
            code must adhere to.
        """
        if not jshint_config:
            options = {"bitwise": allow_bitwise_operators,
                       "freeze": not allow_prototype_overwrite,
                       "curly": force_braces,
                       "eqeqeq": not allow_type_coercion,
                       "futurehostile": not allow_future_identifiers,
                       "notypeof": not allow_typeof,
                       "forin": force_filter_forin,
                       "funcscope": allow_funcscope,
                       "iterator": iterator,
                       "noarg": prohibit_arg,
                       "nocomma": not allow_comma_operator,
                       "nonbsp": not allow_non_breaking_whitespace,
                       "nonew": prohibit_new,
                       "undef": prohibit_undefined,
                       "singleGroups": prohibit_groups,
                       "varstmt": prohibit_variable_statements,
                       "asi": allow_missing_semicolon,
                       "debug": allow_debugger,
                       "boss": allow_assignment_comparisions,
                       "evil": allow_eval,
                       "globalstrict": allow_global_strict,
                       "plusplus": allow_increment,
                       "proto": allow_proto,
                       "scripturl": allow_scripturls,
                       "supernew": allow_singleton,
                       "validthis": allow_this_statements,
                       "withstmt": allow_with_statements,
                       "moz": using_mozilla,
                       "noyield": allow_noyield,
                       "eqnull": allow_eqnull,
                       "lastsemic": allow_last_semicolon,
                       "loopfunc": allow_func_in_loop,
                       "expr": allow_expr_in_assignments,
                       "esnext": use_es6_syntax,
                       "elision": use_es3_array,
                       "mootools": environment_mootools,
                       "couch": environment_couch,
                       "jasmine": environment_jasmine,
                       "jquery": environment_jquery,
                       "node": environment_node,
                       "qunit": environment_qunit,
                       "rhino": environment_rhino,
                       "shelljs": environment_shelljs,
                       "prototypejs": environment_prototypejs,
                       "yui": environment_yui,
                       "mocha": environment_mocha,
                       "module": environment_module,
                       "wsh": environment_wsh,
                       "worker": environment_worker,
                       "nonstandard": environment_nonstandard,
                       "browser": environment_browser,
                       "browserify": environment_browserify,
                       "devel": environment_devel,
                       "dojo": environment_dojo,
                       "typed": environment_typed,
                       "phantom": environment_phantom,
                       "maxerr": 99999,
                       "maxcomplexity": cyclomatic_complexity,
                       "maxdepth": max_depth,
                       "maxparams": max_parameters,
                       "maxstatements": max_statements,
                       "shadow": shadow,
                       "unused": not allow_unused_variables,
                       "latedef": allow_latedef,
                       "esversion": es_version}

            return json.dumps(options)
        else:
            return None

    @staticmethod
    def create_arguments(filename, file, config_file, jshint_config: str=""):
        """
        :param jshint_config:
            The location of the jshintrc config file. If this option is present
            all the above options are not used. Instead the .jshintrc file is
            used as the configuration file.
        """
        args = ('--verbose', filename, '--config')
        if jshint_config:
            args += (jshint_config,)
        else:
            args += (config_file,)
        return args
