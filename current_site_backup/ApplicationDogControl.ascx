<%@ Control Language="C#" AutoEventWireup="True" CodeBehind="ApplicationDogControl.ascx.cs"
	Inherits="TexasRussellRescue.ApplicationDogControl" %>
<%@ Register TagPrefix="telerik" Namespace="Telerik.Web.UI" Assembly="Telerik.Web.UI" %>
<table id="Table2" cellspacing="2" cellpadding="1" width="100%" border="1" rules="none"
	style="border-collapse: collapse">
	<tr class="EditFormHeader">
		<td colspan="2">
			<b>Dog Information</b>
		</td>
	</tr>
	<tr>
		<td>
			<table id="Table3" cellspacing="1" cellpadding="1" width="100%" border="0">
				<tr>
					<td>
					</td>
					<td>
					</td>
				</tr>
				<tr>
					<td>
						Breed:
					</td>
					<td>
						<asp:TextBox ID="txtBreed" runat="server" Text='<%# DataBinder.Eval( Container, "DataItem.Breed" ) %>'>
						</asp:TextBox>
					</td>
				</tr>
				<tr>
					<td>
						Size:
					</td>
					<td>
						<asp:TextBox ID="txtSize" runat="server" Text='<%# DataBinder.Eval( Container, "DataItem.Size") %>'
							TabIndex="1">
						</asp:TextBox>
					</td>
				</tr>
				<tr>
					<td>
						Age:
					</td>
					<td>
						<asp:TextBox ID="txtAge" runat="server" Text='<%# DataBinder.Eval( Container, "DataItem.Age") %>'
							TabIndex="2">
						</asp:TextBox>
					</td>
				</tr>
				<tr>
					<td>
						Gender:
					</td>
					<td>
						<asp:TextBox ID="txtGender" runat="server" Text='<%# DataBinder.Eval( Container, "DataItem.GenderType") %>'
							TabIndex="2">
						</asp:TextBox>
					</td>
				</tr>
				<tr>
					<td>
						Fixed:
					</td>
					<td>
						<asp:TextBox ID="txtFixed" Text='<%# DataBinder.Eval( Container, "DataItem.Fixed") %>'
							runat="server" TextMode="MultiLine" Rows="5" Columns="40" TabIndex="5">
						</asp:TextBox>
					</td>
				</tr>
			</table>
		</td>
		<td>
		</td>
	</tr>
	<tr>
		<td align="right" colspan="2">
			<asp:Button ID="btnUpdate" Text="Update" runat="server" CommandName="Update" Visible='<%# !(DataItem is Telerik.Web.UI.GridInsertionObject) %>'>
			</asp:Button>
			<asp:Button ID="btnInsert" Text="Insert" runat="server" CommandName="PerformInsert"
				Visible='<%# DataItem is Telerik.Web.UI.GridInsertionObject %>'></asp:Button>
			&nbsp;
			<asp:Button ID="btnCancel" Text="Cancel" runat="server" CausesValidation="False"
				CommandName="Cancel"></asp:Button>
		</td>
	</tr>
</table>
