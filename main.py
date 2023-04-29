import isystem.itest as it
import isystem.connect as ic


class TestCustomMethods:

    def __init__(self, connection_mgr: ic.ConnectionMgr, debug_ctrl: ic.CDebugFacade):
        self.connectionMgr = connection_mgr
        self.__dbg = debug_ctrl

    def my_init_test_func(self, a, b):
        print('my_init_test_func:')
        print('    Is target stopped:', self.__dbg.getCPUStatus().isStopped())

        print('    a = ' + str(a))
        print('    b = ' + str(b))

    def my_end_test_func(self, a, b, c):
        print('my_end_test_func:')
        print('    a = ' + str(a))
        print('    b = ' + str(b))
        print('    c = ' + str(c))

    def my_init_target_func(self, a, b):
        print('my_init_target_func:')
        print('    target status:' + self.__dbg.getCPUStatus().toString())
        print('    a = ' + str(a))
        print('    b = ' + str(b))

    def my_restore_target_func(self, param):
        print('my_restore_target_func:')
        print('    ' + param)

    def my_stub_hit_func(self, param):
        print('my_stub_hit_func:')
        print('    ' + str(param))
        # modify stub return value
        testCtrl = ic.CTestCaseController(self.connectionMgr, self._isys_testCaseHandle)
        testCtrl.modify('srv', '144')


def init_target() -> [ic.ConnectionMgr, ic.CDebugFacade]:
    cmgr = ic.ConnectionMgr()
    cmgr.connectMRU('')

    debug_ctrl = ic.CDebugFacade(cmgr)
    debug_ctrl.reset()
    debug_ctrl.runUntilFunction('main')
    debug_ctrl.waitUntilStopped()
    return cmgr, debug_ctrl


def run_test(cmgr: ic.ConnectionMgr, debug_ctrl: ic.CDebugFacade):
    test_case = it.PTestCase(cmgr)
    custom_methods = TestCustomMethods(cmgr, debug_ctrl)

    test_case.itest("""
        func: [init_globals]
        stubs:
        - func: [fibonacci, srv]
          script: [my_stub_hit_func, ["['param1', 'param2']"]] # single param as list of strings
                                                           # double quotes separate YAML [] from Python []
        initFunc: [my_init_test_func, [1, 2]]
        endFunc: [my_end_test_func, [3, 4, '''a''']]
        initTargetFunc: [my_init_target_func, [123, 987]]
        restoreTargetFunc: [my_restore_target_func, ['"paramX"']]
    """, custom_methods)

    results = test_case.getTestResults()

    result = results[0]

    print('\n--------------------------------\n')

    if not result.isError():
        print('OK')
    else:
        print('Test ERROR')
        if result.isException():
            print('Exception: ', result.getExceptionString())

        if result.isExpressionError():
            data_results = ic.StrVector()
            result.getExpressionResults(data_results)
            for expr_result in data_results:
                if len(expr_result) > 0:
                    print(expr_result)

        if result.isCodeCoverageError():
            print('Code Coverage Error')

        if result.isProfilerCodeError():
            print('Profiler Code Error')

        if result.isProfilerDataError():
            print('Profiler Data Error')


def main():
    cmgr, debug_ctrl = init_target()
    print('initialized')
    run_test(cmgr, debug_ctrl)


if __name__ == '__main__':
    main()