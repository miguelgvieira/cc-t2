# Generated from grammarLinguagemLA.g4 by ANTLR 4.13.0
from antlr4 import *
if "." in __name__:
    from .grammarLinguagemLAParser import grammarLinguagemLAParser
else:
    from grammarLinguagemLAParser import grammarLinguagemLAParser

# This class defines a complete listener for a parse tree produced by grammarLinguagemLAParser.
class grammarLinguagemLAListener(ParseTreeListener):

    # Enter a parse tree produced by grammarLinguagemLAParser#programa.
    def enterPrograma(self, ctx:grammarLinguagemLAParser.ProgramaContext):
        pass

    # Exit a parse tree produced by grammarLinguagemLAParser#programa.
    def exitPrograma(self, ctx:grammarLinguagemLAParser.ProgramaContext):
        pass


    # Enter a parse tree produced by grammarLinguagemLAParser#declaracoes.
    def enterDeclaracoes(self, ctx:grammarLinguagemLAParser.DeclaracoesContext):
        pass

    # Exit a parse tree produced by grammarLinguagemLAParser#declaracoes.
    def exitDeclaracoes(self, ctx:grammarLinguagemLAParser.DeclaracoesContext):
        pass


    # Enter a parse tree produced by grammarLinguagemLAParser#decl_local_global.
    def enterDecl_local_global(self, ctx:grammarLinguagemLAParser.Decl_local_globalContext):
        pass

    # Exit a parse tree produced by grammarLinguagemLAParser#decl_local_global.
    def exitDecl_local_global(self, ctx:grammarLinguagemLAParser.Decl_local_globalContext):
        pass


    # Enter a parse tree produced by grammarLinguagemLAParser#declaracao_local.
    def enterDeclaracao_local(self, ctx:grammarLinguagemLAParser.Declaracao_localContext):
        pass

    # Exit a parse tree produced by grammarLinguagemLAParser#declaracao_local.
    def exitDeclaracao_local(self, ctx:grammarLinguagemLAParser.Declaracao_localContext):
        pass


    # Enter a parse tree produced by grammarLinguagemLAParser#variavel.
    def enterVariavel(self, ctx:grammarLinguagemLAParser.VariavelContext):
        pass

    # Exit a parse tree produced by grammarLinguagemLAParser#variavel.
    def exitVariavel(self, ctx:grammarLinguagemLAParser.VariavelContext):
        pass


    # Enter a parse tree produced by grammarLinguagemLAParser#identificador.
    def enterIdentificador(self, ctx:grammarLinguagemLAParser.IdentificadorContext):
        pass

    # Exit a parse tree produced by grammarLinguagemLAParser#identificador.
    def exitIdentificador(self, ctx:grammarLinguagemLAParser.IdentificadorContext):
        pass


    # Enter a parse tree produced by grammarLinguagemLAParser#dimensao.
    def enterDimensao(self, ctx:grammarLinguagemLAParser.DimensaoContext):
        pass

    # Exit a parse tree produced by grammarLinguagemLAParser#dimensao.
    def exitDimensao(self, ctx:grammarLinguagemLAParser.DimensaoContext):
        pass


    # Enter a parse tree produced by grammarLinguagemLAParser#tipo.
    def enterTipo(self, ctx:grammarLinguagemLAParser.TipoContext):
        pass

    # Exit a parse tree produced by grammarLinguagemLAParser#tipo.
    def exitTipo(self, ctx:grammarLinguagemLAParser.TipoContext):
        pass


    # Enter a parse tree produced by grammarLinguagemLAParser#tipo_basico.
    def enterTipo_basico(self, ctx:grammarLinguagemLAParser.Tipo_basicoContext):
        pass

    # Exit a parse tree produced by grammarLinguagemLAParser#tipo_basico.
    def exitTipo_basico(self, ctx:grammarLinguagemLAParser.Tipo_basicoContext):
        pass


    # Enter a parse tree produced by grammarLinguagemLAParser#tipo_basico_ident.
    def enterTipo_basico_ident(self, ctx:grammarLinguagemLAParser.Tipo_basico_identContext):
        pass

    # Exit a parse tree produced by grammarLinguagemLAParser#tipo_basico_ident.
    def exitTipo_basico_ident(self, ctx:grammarLinguagemLAParser.Tipo_basico_identContext):
        pass


    # Enter a parse tree produced by grammarLinguagemLAParser#tipo_estendido.
    def enterTipo_estendido(self, ctx:grammarLinguagemLAParser.Tipo_estendidoContext):
        pass

    # Exit a parse tree produced by grammarLinguagemLAParser#tipo_estendido.
    def exitTipo_estendido(self, ctx:grammarLinguagemLAParser.Tipo_estendidoContext):
        pass


    # Enter a parse tree produced by grammarLinguagemLAParser#valor_constante.
    def enterValor_constante(self, ctx:grammarLinguagemLAParser.Valor_constanteContext):
        pass

    # Exit a parse tree produced by grammarLinguagemLAParser#valor_constante.
    def exitValor_constante(self, ctx:grammarLinguagemLAParser.Valor_constanteContext):
        pass


    # Enter a parse tree produced by grammarLinguagemLAParser#registro.
    def enterRegistro(self, ctx:grammarLinguagemLAParser.RegistroContext):
        pass

    # Exit a parse tree produced by grammarLinguagemLAParser#registro.
    def exitRegistro(self, ctx:grammarLinguagemLAParser.RegistroContext):
        pass


    # Enter a parse tree produced by grammarLinguagemLAParser#declaracao_global.
    def enterDeclaracao_global(self, ctx:grammarLinguagemLAParser.Declaracao_globalContext):
        pass

    # Exit a parse tree produced by grammarLinguagemLAParser#declaracao_global.
    def exitDeclaracao_global(self, ctx:grammarLinguagemLAParser.Declaracao_globalContext):
        pass


    # Enter a parse tree produced by grammarLinguagemLAParser#parametro.
    def enterParametro(self, ctx:grammarLinguagemLAParser.ParametroContext):
        pass

    # Exit a parse tree produced by grammarLinguagemLAParser#parametro.
    def exitParametro(self, ctx:grammarLinguagemLAParser.ParametroContext):
        pass


    # Enter a parse tree produced by grammarLinguagemLAParser#parametros.
    def enterParametros(self, ctx:grammarLinguagemLAParser.ParametrosContext):
        pass

    # Exit a parse tree produced by grammarLinguagemLAParser#parametros.
    def exitParametros(self, ctx:grammarLinguagemLAParser.ParametrosContext):
        pass


    # Enter a parse tree produced by grammarLinguagemLAParser#corpo.
    def enterCorpo(self, ctx:grammarLinguagemLAParser.CorpoContext):
        pass

    # Exit a parse tree produced by grammarLinguagemLAParser#corpo.
    def exitCorpo(self, ctx:grammarLinguagemLAParser.CorpoContext):
        pass


    # Enter a parse tree produced by grammarLinguagemLAParser#cmd.
    def enterCmd(self, ctx:grammarLinguagemLAParser.CmdContext):
        pass

    # Exit a parse tree produced by grammarLinguagemLAParser#cmd.
    def exitCmd(self, ctx:grammarLinguagemLAParser.CmdContext):
        pass


    # Enter a parse tree produced by grammarLinguagemLAParser#cmdleia.
    def enterCmdleia(self, ctx:grammarLinguagemLAParser.CmdleiaContext):
        pass

    # Exit a parse tree produced by grammarLinguagemLAParser#cmdleia.
    def exitCmdleia(self, ctx:grammarLinguagemLAParser.CmdleiaContext):
        pass


    # Enter a parse tree produced by grammarLinguagemLAParser#cmdescreva.
    def enterCmdescreva(self, ctx:grammarLinguagemLAParser.CmdescrevaContext):
        pass

    # Exit a parse tree produced by grammarLinguagemLAParser#cmdescreva.
    def exitCmdescreva(self, ctx:grammarLinguagemLAParser.CmdescrevaContext):
        pass


    # Enter a parse tree produced by grammarLinguagemLAParser#cmdse.
    def enterCmdse(self, ctx:grammarLinguagemLAParser.CmdseContext):
        pass

    # Exit a parse tree produced by grammarLinguagemLAParser#cmdse.
    def exitCmdse(self, ctx:grammarLinguagemLAParser.CmdseContext):
        pass


    # Enter a parse tree produced by grammarLinguagemLAParser#cmdcaso.
    def enterCmdcaso(self, ctx:grammarLinguagemLAParser.CmdcasoContext):
        pass

    # Exit a parse tree produced by grammarLinguagemLAParser#cmdcaso.
    def exitCmdcaso(self, ctx:grammarLinguagemLAParser.CmdcasoContext):
        pass


    # Enter a parse tree produced by grammarLinguagemLAParser#cmdpara.
    def enterCmdpara(self, ctx:grammarLinguagemLAParser.CmdparaContext):
        pass

    # Exit a parse tree produced by grammarLinguagemLAParser#cmdpara.
    def exitCmdpara(self, ctx:grammarLinguagemLAParser.CmdparaContext):
        pass


    # Enter a parse tree produced by grammarLinguagemLAParser#cmdenquanto.
    def enterCmdenquanto(self, ctx:grammarLinguagemLAParser.CmdenquantoContext):
        pass

    # Exit a parse tree produced by grammarLinguagemLAParser#cmdenquanto.
    def exitCmdenquanto(self, ctx:grammarLinguagemLAParser.CmdenquantoContext):
        pass


    # Enter a parse tree produced by grammarLinguagemLAParser#cmdfaca.
    def enterCmdfaca(self, ctx:grammarLinguagemLAParser.CmdfacaContext):
        pass

    # Exit a parse tree produced by grammarLinguagemLAParser#cmdfaca.
    def exitCmdfaca(self, ctx:grammarLinguagemLAParser.CmdfacaContext):
        pass


    # Enter a parse tree produced by grammarLinguagemLAParser#cmdatribuicao.
    def enterCmdatribuicao(self, ctx:grammarLinguagemLAParser.CmdatribuicaoContext):
        pass

    # Exit a parse tree produced by grammarLinguagemLAParser#cmdatribuicao.
    def exitCmdatribuicao(self, ctx:grammarLinguagemLAParser.CmdatribuicaoContext):
        pass


    # Enter a parse tree produced by grammarLinguagemLAParser#cmdchamada.
    def enterCmdchamada(self, ctx:grammarLinguagemLAParser.CmdchamadaContext):
        pass

    # Exit a parse tree produced by grammarLinguagemLAParser#cmdchamada.
    def exitCmdchamada(self, ctx:grammarLinguagemLAParser.CmdchamadaContext):
        pass


    # Enter a parse tree produced by grammarLinguagemLAParser#cmdretorno.
    def enterCmdretorno(self, ctx:grammarLinguagemLAParser.CmdretornoContext):
        pass

    # Exit a parse tree produced by grammarLinguagemLAParser#cmdretorno.
    def exitCmdretorno(self, ctx:grammarLinguagemLAParser.CmdretornoContext):
        pass


    # Enter a parse tree produced by grammarLinguagemLAParser#selecao.
    def enterSelecao(self, ctx:grammarLinguagemLAParser.SelecaoContext):
        pass

    # Exit a parse tree produced by grammarLinguagemLAParser#selecao.
    def exitSelecao(self, ctx:grammarLinguagemLAParser.SelecaoContext):
        pass


    # Enter a parse tree produced by grammarLinguagemLAParser#item_selecao.
    def enterItem_selecao(self, ctx:grammarLinguagemLAParser.Item_selecaoContext):
        pass

    # Exit a parse tree produced by grammarLinguagemLAParser#item_selecao.
    def exitItem_selecao(self, ctx:grammarLinguagemLAParser.Item_selecaoContext):
        pass


    # Enter a parse tree produced by grammarLinguagemLAParser#constantes.
    def enterConstantes(self, ctx:grammarLinguagemLAParser.ConstantesContext):
        pass

    # Exit a parse tree produced by grammarLinguagemLAParser#constantes.
    def exitConstantes(self, ctx:grammarLinguagemLAParser.ConstantesContext):
        pass


    # Enter a parse tree produced by grammarLinguagemLAParser#numero_intervalo.
    def enterNumero_intervalo(self, ctx:grammarLinguagemLAParser.Numero_intervaloContext):
        pass

    # Exit a parse tree produced by grammarLinguagemLAParser#numero_intervalo.
    def exitNumero_intervalo(self, ctx:grammarLinguagemLAParser.Numero_intervaloContext):
        pass


    # Enter a parse tree produced by grammarLinguagemLAParser#op_unario.
    def enterOp_unario(self, ctx:grammarLinguagemLAParser.Op_unarioContext):
        pass

    # Exit a parse tree produced by grammarLinguagemLAParser#op_unario.
    def exitOp_unario(self, ctx:grammarLinguagemLAParser.Op_unarioContext):
        pass


    # Enter a parse tree produced by grammarLinguagemLAParser#exp_aritmetica.
    def enterExp_aritmetica(self, ctx:grammarLinguagemLAParser.Exp_aritmeticaContext):
        pass

    # Exit a parse tree produced by grammarLinguagemLAParser#exp_aritmetica.
    def exitExp_aritmetica(self, ctx:grammarLinguagemLAParser.Exp_aritmeticaContext):
        pass


    # Enter a parse tree produced by grammarLinguagemLAParser#termo.
    def enterTermo(self, ctx:grammarLinguagemLAParser.TermoContext):
        pass

    # Exit a parse tree produced by grammarLinguagemLAParser#termo.
    def exitTermo(self, ctx:grammarLinguagemLAParser.TermoContext):
        pass


    # Enter a parse tree produced by grammarLinguagemLAParser#fator.
    def enterFator(self, ctx:grammarLinguagemLAParser.FatorContext):
        pass

    # Exit a parse tree produced by grammarLinguagemLAParser#fator.
    def exitFator(self, ctx:grammarLinguagemLAParser.FatorContext):
        pass


    # Enter a parse tree produced by grammarLinguagemLAParser#op1.
    def enterOp1(self, ctx:grammarLinguagemLAParser.Op1Context):
        pass

    # Exit a parse tree produced by grammarLinguagemLAParser#op1.
    def exitOp1(self, ctx:grammarLinguagemLAParser.Op1Context):
        pass


    # Enter a parse tree produced by grammarLinguagemLAParser#op2.
    def enterOp2(self, ctx:grammarLinguagemLAParser.Op2Context):
        pass

    # Exit a parse tree produced by grammarLinguagemLAParser#op2.
    def exitOp2(self, ctx:grammarLinguagemLAParser.Op2Context):
        pass


    # Enter a parse tree produced by grammarLinguagemLAParser#op3.
    def enterOp3(self, ctx:grammarLinguagemLAParser.Op3Context):
        pass

    # Exit a parse tree produced by grammarLinguagemLAParser#op3.
    def exitOp3(self, ctx:grammarLinguagemLAParser.Op3Context):
        pass


    # Enter a parse tree produced by grammarLinguagemLAParser#parcela.
    def enterParcela(self, ctx:grammarLinguagemLAParser.ParcelaContext):
        pass

    # Exit a parse tree produced by grammarLinguagemLAParser#parcela.
    def exitParcela(self, ctx:grammarLinguagemLAParser.ParcelaContext):
        pass


    # Enter a parse tree produced by grammarLinguagemLAParser#parcela_unario.
    def enterParcela_unario(self, ctx:grammarLinguagemLAParser.Parcela_unarioContext):
        pass

    # Exit a parse tree produced by grammarLinguagemLAParser#parcela_unario.
    def exitParcela_unario(self, ctx:grammarLinguagemLAParser.Parcela_unarioContext):
        pass


    # Enter a parse tree produced by grammarLinguagemLAParser#parcela_nao_unario.
    def enterParcela_nao_unario(self, ctx:grammarLinguagemLAParser.Parcela_nao_unarioContext):
        pass

    # Exit a parse tree produced by grammarLinguagemLAParser#parcela_nao_unario.
    def exitParcela_nao_unario(self, ctx:grammarLinguagemLAParser.Parcela_nao_unarioContext):
        pass


    # Enter a parse tree produced by grammarLinguagemLAParser#exp_relacional.
    def enterExp_relacional(self, ctx:grammarLinguagemLAParser.Exp_relacionalContext):
        pass

    # Exit a parse tree produced by grammarLinguagemLAParser#exp_relacional.
    def exitExp_relacional(self, ctx:grammarLinguagemLAParser.Exp_relacionalContext):
        pass


    # Enter a parse tree produced by grammarLinguagemLAParser#op_relacional.
    def enterOp_relacional(self, ctx:grammarLinguagemLAParser.Op_relacionalContext):
        pass

    # Exit a parse tree produced by grammarLinguagemLAParser#op_relacional.
    def exitOp_relacional(self, ctx:grammarLinguagemLAParser.Op_relacionalContext):
        pass


    # Enter a parse tree produced by grammarLinguagemLAParser#expressao.
    def enterExpressao(self, ctx:grammarLinguagemLAParser.ExpressaoContext):
        pass

    # Exit a parse tree produced by grammarLinguagemLAParser#expressao.
    def exitExpressao(self, ctx:grammarLinguagemLAParser.ExpressaoContext):
        pass


    # Enter a parse tree produced by grammarLinguagemLAParser#termo_logico.
    def enterTermo_logico(self, ctx:grammarLinguagemLAParser.Termo_logicoContext):
        pass

    # Exit a parse tree produced by grammarLinguagemLAParser#termo_logico.
    def exitTermo_logico(self, ctx:grammarLinguagemLAParser.Termo_logicoContext):
        pass


    # Enter a parse tree produced by grammarLinguagemLAParser#fator_logico.
    def enterFator_logico(self, ctx:grammarLinguagemLAParser.Fator_logicoContext):
        pass

    # Exit a parse tree produced by grammarLinguagemLAParser#fator_logico.
    def exitFator_logico(self, ctx:grammarLinguagemLAParser.Fator_logicoContext):
        pass


    # Enter a parse tree produced by grammarLinguagemLAParser#parcela_logica.
    def enterParcela_logica(self, ctx:grammarLinguagemLAParser.Parcela_logicaContext):
        pass

    # Exit a parse tree produced by grammarLinguagemLAParser#parcela_logica.
    def exitParcela_logica(self, ctx:grammarLinguagemLAParser.Parcela_logicaContext):
        pass


    # Enter a parse tree produced by grammarLinguagemLAParser#op_logico_1.
    def enterOp_logico_1(self, ctx:grammarLinguagemLAParser.Op_logico_1Context):
        pass

    # Exit a parse tree produced by grammarLinguagemLAParser#op_logico_1.
    def exitOp_logico_1(self, ctx:grammarLinguagemLAParser.Op_logico_1Context):
        pass


    # Enter a parse tree produced by grammarLinguagemLAParser#op_logico_2.
    def enterOp_logico_2(self, ctx:grammarLinguagemLAParser.Op_logico_2Context):
        pass

    # Exit a parse tree produced by grammarLinguagemLAParser#op_logico_2.
    def exitOp_logico_2(self, ctx:grammarLinguagemLAParser.Op_logico_2Context):
        pass



del grammarLinguagemLAParser