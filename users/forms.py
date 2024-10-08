x�VM��0�9�B5�=9fCi!8���C鞃lObY2#9a��'���'�u�����o!>K�y��<�^"u_�}���3�y��"[���5�a�m�Y0�[��3B��ʀ=(��O�V�&�-���R�%C����	&����`kćԘa!���e��Ċ��3R�,
��o�\cAq���@j�����䏓)������V@qD�=��+��:�6�t��2S���KP��~z�{28�֡��Uy�!7̭*�x�<�f��(���!j�rkq����k��~�"Apt�M�Q�mOk�;����n2 D���3hޏ����dsVf����}���I*���T��?&\�[��jD��IRc ��H�j��hh��hH�C�����4h�[S]�vw�.1��)����)Ev��Z��:]@�G&��-��Ͽ�5!vW�(�>z�t�5f���2u�97��ͯ���w���JoT���#���㚵�G3���6�%����̾�@~�J
A^h�eECgT�U��~�Z�����D��in�ح��^�u-ͅ�ͬ$�@��s�'raL��p�	���REVgڐ/4,��#���WTҙ�ú�=�Sv����h3�լ�B��                                                                                                                                                                                                                                                                                                                                                                                                         lse, label='Apellido')
    rut = forms.CharField(max_length=12, label='RUT', help_text='Ingrese su RUT sin puntos ni guiones')
    user_type = forms.ChoiceField(choices=Profile.USER_TYPE_CHOICES, label='Tipo de Usuario')

    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name', 'rut', 'user_type', 'password1', 'password2')

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data['email']
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        if commit:
            user.save()
            profile, created = Profile.objects.get_or_create(user=user)
            profile.rut = self.cleaned_data['rut']
            profile.user_type = self.cleaned_data['user_type']
            profile.save()
        return user