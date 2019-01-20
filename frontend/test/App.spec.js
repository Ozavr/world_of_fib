import { mount } from '@vue/test-utils'
import App from '../src/App.vue'


describe('App.vue', () => {
    it('нельзя использовать форму без данных', () => {
        const wrapper = mount(App);
        wrapper.find('#for').setValue('');
        wrapper.find('input#to').setValue('');
        wrapper.find('button').trigger('click')
        expect(wrapper.find('result__text').text().toMatch('1'));
    })
})